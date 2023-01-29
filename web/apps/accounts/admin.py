from django.contrib import admin

from .forms import UserAccountChangeForm, UserAccountCreationForm
from .models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    form = UserAccountChangeForm
    add_form = UserAccountCreationForm
