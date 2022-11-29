from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import Group

from profiles.models import ProfileModel

from utilities.constants import (
    ApiResponseMessages,
    account_types,
    e_account_types
)


def check_groups(request, ):
    valid = True
    data = None

    if request.data['account_type'] == account_types['MANAGER']:
        authorized_group, created = Group.objects.get_or_create(
            name=e_account_types[account_types['SUPER_ADMIN']])

        if not authorized_group in request.user.groups.all():
            valid = False
            data = {
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": ApiResponseMessages['UNATHORIZED_ERROR']
            }
    elif request.data['account_type'] == account_types['EMPLOYEE']:
        super_admin_group, created = Group.objects.get_or_create(
            name=e_account_types[account_types['SUPER_ADMIN']])
        manager_group, created = Group.objects.get_or_create(
            name=e_account_types[account_types['MANAGER']])

        if super_admin_group not in request.user.groups.all() and manager_group not in request.user.groups.all():
            valid = False
            data = {
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": ApiResponseMessages['UNATHORIZED_ERROR']
            }
    else:
        valid = False
        data = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": ApiResponseMessages['INVALID_ACCOUNT_TYPE']
        }

    return valid, data


def user_creation_validation_decorator(func):
    def inner_func(view_instance, request, *args, **kwargs):
        valid, data = check_groups(request)

        if not valid:
            return Response(data, status=data["status"])

        return func(view_instance, request, *args, **kwargs)

    return inner_func
