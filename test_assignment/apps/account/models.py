from django.contrib.auth.models import AbstractUser
from django.db import models

from test_assignment.apps.account.managers import CustomUserManager


class User(AbstractUser):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Tweet(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=160)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
