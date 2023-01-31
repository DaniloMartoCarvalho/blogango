from apps.articles.models import Article
from django.test import TestCase
from django.urls import reverse

from ..factory.articles import ArticleFactory


class ArticleListViewTestCase(TestCase):
    def setUp(self) -> None:
        ArticleFactory()
        self.request = self.client.get(reverse("articles:list"))

    def test_the_request_status_code(self) -> None:
        self.assertEqual(self.request.status_code, 200)

    def test_the_name_of_the_template_used_to_render_the_response(self) -> None:
        self.assertTemplateUsed(self.request, "articles/article_list.html")

    def test_if_each_item_in_the_list_is_an_instance_of_the_Article_model(self) -> None:
        article = self.request.context["object_list"][0]
        self.assertTrue(isinstance(article, Article))


class ArticleListviewWhenIsNotPaginated(TestCase):
    def setUp(self):
        ArticleFactory()
        self.request = self.client.get(reverse("articles:list"))

    def test_articles_are_not_paginated_when_there_are_less_than_10_articles_published(
        self,
    ) -> None:
        self.assertFalse(self.request.context["is_paginated"])


class ArticleListviewWhenIsPaginated(TestCase):
    def setUp(self):
        for _ in range(46):
            ArticleFactory()

        self.request = self.client.get(reverse("articles:list"))

    def test_articles_are_paginated_when_there_are_more_than_10_articles_published(
        self,
    ) -> None:

        self.assertTrue(self.request.context["is_paginated"])

    def test_if_10_articles_are_listed_per_page(self) -> None:
        self.assertEqual(len(self.request.context["object_list"]), 10)


class ArticleDetailViewTestCase(TestCase):
    def setUp(self) -> None:
        article = ArticleFactory()
        self.request = self.client.get(article.get_absolute_url())

    def test_the_request_status_code(self) -> None:
        self.assertEqual(self.request.status_code, 200)

    def test_the_name_of_the_template_used_to_render_the_response(self) -> None:
        self.assertTemplateUsed(self.request, "articles/article_detail.html")

    def test_if_each_item_in_the_list_is_an_instance_of_the_Article_model(self) -> None:
        article = self.request.context["object"]
        self.assertTrue(isinstance(article, Article))
