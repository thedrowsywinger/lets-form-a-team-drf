from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from uuid import uuid4

from core.managers import CustomUserManager

# Create your models here.


class CustomAuthUserModel(AbstractUser, PermissionsMixin):
    userId = models.CharField(
        max_length=16, default=uuid4, primary_key=True, editable=False)
    username = models.CharField(
        max_length=16, unique=True, null=False, blank=False)
    email = models.EmailField(
        max_length=100, unique=True, null=False, blank=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Custom User Model"
