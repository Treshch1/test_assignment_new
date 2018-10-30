from django.contrib.auth.models import AbstractUser
from django.db import models

from test_assignment.apps.account.managers import CustomUserManager


class User(AbstractUser):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150)
    following = models.ManyToManyField('self', blank=True)
    tweets_counter = models.PositiveIntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
