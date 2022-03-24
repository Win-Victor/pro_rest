from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import ProUser


class DRFUserAdmin(UserAdmin):
    model = ProUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']


admin.site.register(ProUser, DRFUserAdmin)
