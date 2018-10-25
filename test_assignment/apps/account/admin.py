from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from test_assignment.apps.account.models import Tweet, User


admin.site.register(User, UserAdmin)
admin.site.register(Tweet)
