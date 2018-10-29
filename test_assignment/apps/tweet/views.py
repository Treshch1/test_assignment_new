from django.urls import reverse_lazy
from django.views.generic import CreateView

from test_assignment.apps.tweet.forms import TweetForm
from test_assignment.apps.tweet.models import Tweet


class TweetView(CreateView):
    template_name = 'base.html'
    form_class = TweetForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        tweets = []
        user = self.request.user

        if user.is_authenticated:
            tweets = Tweet.objects.filter(user=user).order_by('-datetime_created')

        return {'tweets': tweets, 'form': self.form_class, 'counter': user.tweets_counter}

    def form_valid(self, form):
        tweet = form.save(commit=False)
        tweet.user = self.request.user
        tweet.save()

        return super(TweetView, self).form_valid(form)
