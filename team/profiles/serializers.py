from rest_framework import serializers

from profiles.models import ProfileModel

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileModel
        fields = ['name']