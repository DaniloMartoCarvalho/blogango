from django.test import TestCase
from django.urls import reverse

from ..models import Article
from .factory import ArticleFactory


class TestArticleListView(TestCase):
    def setUp(self) -> None:
        self.request = self.client.get(reverse("articles:article_list"))

    def test_the_template_name_used(self) -> None:
        self.assertTemplateUsed(self.request, "article/article_list.html")

    def test_only_articles_with_published_status_are_displayed(self) -> None:
        ArticleFactory(status=Article.Status.DRAFT)
        ArticleFactory(status=Article.Status.PUBLISHED)
        request = self.client.get(reverse("articles:article_list"))
        self.assertEqual(len(request.context["object_list"]), 1)


class TestArticleDetailView(TestCase):
    def setUp(self) -> None:
        article = ArticleFactory(status=Article.Status.PUBLISHED)
        self.request = self.client.get(
            reverse("articles:article_detail", kwargs={"pk": article.pk})
        )

    def test_the_template_name_used(self) -> None:
        self.assertTemplateUsed(self.request, "article/article_detail.html")
