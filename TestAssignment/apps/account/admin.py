from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from TestAssignment.apps.account.models import User


admin.site.register(User, UserAdmin)
