from apps.articles.models import Article
from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from ..factory.articles import ArticleFactory


class ArticleModelTestCase(TestCase):
    def test_if_the_article_is_saved(self) -> None:
        ArticleFactory()
        self.assertEqual(Article.objects.count(), 1)

    def test_the_slug_is_obtained_from_the_title(self) -> None:
        article = ArticleFactory()
        slug = slugify(article.title)
        self.assertEqual(article.slug, slug)

    def test_the_absolute_URL_of_an_article(self) -> None:
        article = ArticleFactory()

        datas = {
            "year": article.published.year,
            "month": article.published.month,
            "day": article.published.day,
            "article_slug": article.slug,
        }

        url = reverse("articles:detail", kwargs=datas)
        self.assertEqual(article.get_absolute_url(), url)
