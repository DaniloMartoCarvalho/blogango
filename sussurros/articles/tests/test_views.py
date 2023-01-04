from django.test import TestCase
from django.urls import reverse


class TestArticleListView(TestCase):
    def setUp(self) -> None:
        self.request = self.client.get(reverse("articles:article_list"))

    def test_the_template_name_used(self) -> None:
        self.assertTemplateUsed(self.request, "article/article_list.html")


class TestArticleDetailView(TestCase):
    def setUp(self) -> None:
        self.request = self.client.get(
            reverse("articles:article_detail", kwargs={"pk": 1})
        )

    def test_the_template_name_used(self) -> None:
        self.assertTemplateUsed(self.request, "article/article_detail.html")
