from django.forms import ModelForm

from test_assignment.apps.tweet.models import Tweet


class TweetForm(ModelForm):

    class Meta:
        model = Tweet
        fields = ['text', ]
