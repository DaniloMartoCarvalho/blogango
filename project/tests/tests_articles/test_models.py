from apps.articles.models import Article
from django.test import TestCase

from ..factory.articles import ArticleFactory


class ArticleModelTestCase(TestCase):
    def test_if_the_article_is_saved(self) -> None:
        ArticleFactory()
        self.assertEqual(Article.objects.count(), 1)
