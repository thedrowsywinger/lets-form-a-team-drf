from multiprocessing.managers import BaseManager
from django.contrib.auth.base_user import BaseUserManager

from utilities.constants import (
    ApiResponseMessages
)


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
          Creates a custom user with the given fields
        """

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password=password
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
