from cProfile import Profile
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db import transaction
from django.contrib.auth.models import Group

from core.models import CustomAuthUserModel
from profiles.models import ProfileModel

from utilities.required_fields import (
    user_sign_up_required_fields
)
from utilities.constants import (
    ApiResponseMessages,
    account_types,
    field_missing_error_message,
    e_account_types
)

# super_admin_group, created = Group.objects.get_or_create(
#     name=e_account_types['1'])
# manager_group, created = Group.objects.get_or_create(name=e_account_types['2'])
# employee_group, created = Group.objects.get_or_create(
#     name=e_account_types['3'])


class UserSignUp(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'lets go'}
        return Response(content)

    @transaction.atomic
    def post(self, request):
        for field in user_sign_up_required_fields:
            data = {
                "status": status.HTTP_406_NOT_ACCEPTABLE,
                "message": field_missing_error_message(field)
            }
            if field not in request.data:
                return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
        auth_user = CustomAuthUserModel.objects.create_user(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password']
        )
        profile = ProfileModel.objects.create(
            name=request.data['name'],
            user=auth_user
        )
        group, created = Group.objects.get_or_create(
            name=e_account_types[request.data['account_type']])
        auth_user.groups.add(group)

        data = {
            "status": status.HTTP_200_OK,
            "message": "Success"
        }
        return Response(data, status=status.HTTP_200_OK)
