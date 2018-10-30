from django.contrib.auth import authenticate, login, views
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from test_assignment.apps.account.forms import CustomUserCreationForm
from test_assignment.apps.account.models import User


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


class FollowView(View):
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        current_user_id = self.request.user.id
        user_to_follow_id = kwargs.get('user_id')

        User.objects.get(id=current_user_id).following.add(user_to_follow_id)

        return HttpResponseRedirect(self.success_url)
