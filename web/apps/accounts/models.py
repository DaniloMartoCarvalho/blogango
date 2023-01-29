from django.contrib.auth.models import AbstractUser, UserManager


class UserAccountManager(UserManager):
    pass


class UserAccount(AbstractUser):
    objects = UserAccountManager()
