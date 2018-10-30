from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView

from test_assignment.apps.account.models import User
from test_assignment.apps.tweet.forms import TweetForm
from test_assignment.apps.tweet.models import Tweet


class TweetView(CreateView):
    template_name = 'base.html'
    form_class = TweetForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        user = self.request.user

        if user.is_authenticated:

            users_to_follow = User.objects.exclude(
                Q(pk=user.pk) | Q(pk__in=user.following.all())
            ).values('pk', 'email')

            tweets = Tweet.objects.filter(
                Q(user=user) | Q(user__in=user.following.all())
            ).order_by('-datetime_created').values('text', 'user__email', 'datetime_created')

            counter = user.tweets_counter

            return {'tweets': tweets, 'form': self.form_class, 'counter': counter, 'users': users_to_follow}

        return {}

    def form_valid(self, form):
        tweet = form.save(commit=False)
        tweet.user = self.request.user
        tweet.save()

        return super(TweetView, self).form_valid(form)
