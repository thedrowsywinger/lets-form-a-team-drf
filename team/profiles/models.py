from django.db import models

from core.models import CustomAuthUserModel

# Create your models here.


class ProfileModel(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomAuthUserModel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
