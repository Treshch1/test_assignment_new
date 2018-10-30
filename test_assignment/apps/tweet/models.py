from django.db import models
from django.db.models import F
from django.db.models.signals import pre_save
from django.dispatch import receiver

from test_assignment.apps.account.models import User


class Tweet(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    text = models.CharField(max_length=160)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


@receiver(pre_save, sender=Tweet)
def increase_counter(sender, **kwargs):
    user = kwargs['instance'].user

    user.tweets_counter = F('tweets_counter') + 1
    user.save()
