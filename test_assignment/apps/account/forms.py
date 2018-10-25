from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from test_assignment.apps.account.models import Tweet, User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', ]


class TweetForm(ModelForm):

    class Meta:
        model = Tweet
        fields = ['text', ]
