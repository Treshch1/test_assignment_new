from django.contrib.auth import authenticate, login, views
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from TestAssignment.apps.account.forms import CustomUserCreationForm


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
