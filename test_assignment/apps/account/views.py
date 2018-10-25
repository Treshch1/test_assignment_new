from django.contrib.auth import authenticate, login, views
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from test_assignment.apps.account.forms import CustomUserCreationForm, TweetForm
from test_assignment.apps.account.models import Tweet


class SignUpView(FormView):

    form_class = CustomUserCreationForm
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        user = authenticate(email=email, password=password)
        login(self.request, user)

        return HttpResponseRedirect(reverse_lazy('home'))


class LoginView(views.LoginView):

    template_name = 'login.html'


class LogoutView(views.LogoutView):

    next_page = reverse_lazy('home')


class TweetView(FormView):
    template_name = 'base.html'
    form_class = TweetForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        tweets = []
        user = self.request.user

        if user.is_authenticated:
            tweets = Tweet.objects.filter(user=user).order_by('-datetime_created')

        return {'tweets': tweets, 'form': self.form_class}

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()

        return super(TweetView, self).form_valid(form)
