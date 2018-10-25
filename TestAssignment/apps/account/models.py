from django.contrib.auth.models import AbstractUser
from django.db import models

from TestAssignment.apps.account.managers import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
