from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from ..models import Article
from .factory import ArticleFactory


class TestArticleModel(TestCase):
    def setUp(self) -> None:
        self.article = ArticleFactory()

    def test_the_absolute_URL_for_an_article(self) -> None:
        data = {
            "pk": self.article.pk,
        }

        url = reverse("articles:article_detail", kwargs=data)
        self.assertEqual(self.article.get_absolute_url(), url)

    def test_the_slug_is_taken_from_the_title(self) -> None:
        slug = slugify(self.article.title)
        self.assertEqual(self.article.slug, slug)

    def test_slug_does_not_change_when_title_changes(self) -> None:
        self.article.title = f"{self.article.title} 2"
        self.article.save()

        slug = slugify(self.article.title)
        self.assertNotEqual(self.article.slug, slug)


class TestArticleManager(TestCase):
    def test_only_articles_with_published_status_are_listed(self) -> None:
        ArticleFactory(status=Article.Status.DRAFT)
        ArticleFactory(status=Article.Status.PUBLISHED)
        self.assertEqual(Article.objects.published().count(), 1)
