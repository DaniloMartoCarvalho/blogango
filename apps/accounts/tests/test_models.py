from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import UserAccounts


class TestUserAccounts(TestCase):
    def test_the_user_model_default_is_the_custom_user_model(self) -> None:
        self.assertEqual(get_user_model(), UserAccounts)
