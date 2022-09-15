from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db import transaction
from core.models import CustomAuthUserModel
from profiles.models import ProfileModel

from utilities.required_fields import (
    user_sign_up_required_fields
)
from utilities.constants import (
    ApiResponseMessages,
    account_types,
    field_missing_error_message
)


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
        auth_user = CustomAuthUserModel(
            {
                "email": request.data['email'],
                "password": request.data['password']
            }
        )
        auth_user.save()
        print(auth_user)
        data = {
            "status": status.HTTP_200_OK,
            "message": "Success"
        }
        return Response(data, status=status.HTTP_200_OK)
