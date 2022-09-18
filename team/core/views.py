from cProfile import Profile
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db import transaction
from django.contrib.auth.models import Group

from core.models import CustomAuthUserModel
from profiles.models import ProfileModel

from core.serializers import (
    AuthUserSerializer,
    ProfileSerializer
)

from core.decorators import check_groups_decorator

from utilities.required_fields import (
    user_sign_up_required_fields
)
from utilities.constants import (
    ApiResponseMessages,
    account_types,
    field_missing_error_message,
    e_account_types
)


class UserSignUp(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'lets go'}
        return Response(content)

    @check_groups_decorator
    def post(self, request):

        with transaction.atomic():
            auth_user_serializer = AuthUserSerializer(data=request.data)
            if auth_user_serializer.is_valid():
                user_instance = auth_user_serializer.save()
                profile_serializer = ProfileSerializer(
                    data={"name": request.data['name'], "user": user_instance.userId})
                if profile_serializer.is_valid():
                    profile_serializer.save()
                else:
                    data = {
                        "status": status.HTTP_400_BAD_REQUEST,
                        "details": profile_serializer.errors
                    }
                    return Response(data, status=data['status'])
                group, created = Group.objects.get_or_create(
                    name=e_account_types[request.data['account_type']])
                user_instance.groups.add(group)
            else:
                data = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "details": auth_user_serializer.errors
                }
                return Response(data, status=data['status'])

        data = {
            "status": status.HTTP_200_OK,
            "message": "Success"
        }
        return Response(data, status=status.HTTP_200_OK)


class TestView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):

        print("ME IN")
        print(request.user.userId)

        data = {

        }
        return Response(data, status=status.HTTP_200_OK)
