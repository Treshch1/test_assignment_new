from django.contrib.auth.forms import UserCreationForm

from TestAssignment.apps.account.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", )
