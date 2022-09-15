from django.db import models
from django.contrib.auth.models import AbstractUser

from uuid import uuid4

from core.managers import CustomUserManager

# Create your models here.


class CustomAuthUserModel(AbstractUser):
    id = models.IntegerField(primary_key=True, unique=True)
    username = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects: CustomUserManager

    def __str__(self):
        return self.username
