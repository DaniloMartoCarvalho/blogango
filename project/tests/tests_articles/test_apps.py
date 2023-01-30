from django.apps import apps
from django.test import TestCase


class ArticlesAppTestCase9(TestCase):
    def test_articles_app_exists(self) -> None:
        self.assertIn("articles", apps.app_configs)
