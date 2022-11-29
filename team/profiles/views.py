from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from profiles.models import ProfileModel
class ProfileView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):

        id = request.GET["id"]

        if (id is not None):
            profile = ProfileModel.objects.get(id=id)
            return Response(
                {
                    "message": "Successful",
                    "data": profile
                }
            )
            
        else:

            profiles = ProfileModel.objects.all()
            return Response(
                {
                    "message": "Successful",
                    "data": profiles
                }
            )