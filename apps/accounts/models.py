"""Accounts models"""

from django.contrib.auth.models import AbstractUser, UserManager


class UserAccountsManager(UserManager):
    pass


class UserAccounts(AbstractUser):
    """User accounts model"""

    objects = UserAccountsManager()
