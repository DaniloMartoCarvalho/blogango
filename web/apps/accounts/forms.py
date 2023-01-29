from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import UserAccount


class UserAccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserAccount


class UserAccountChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserAccount
