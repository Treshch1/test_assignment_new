from django.urls import path

from test_assignment.apps.tweet.views import TweetView


urlpatterns = [
    path('', TweetView.as_view(), name='home'),
]
