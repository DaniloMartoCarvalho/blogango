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


class ArticleDetailViewTestCase(TestCase):
    def setUp(self) -> None:
        article = ArticleFactory()

        datas = {
            "pk": article.pk,
        }

        self.request = self.client.get(reverse("articles:detail", kwargs=datas))

    def test_the_request_status_code(self) -> None:
        self.assertEqual(self.request.status_code, 200)

    def test_the_name_of_the_template_used_to_render_the_response(self) -> None:
        self.assertTemplateUsed(self.request, "articles/article_detail.html")

    def test_if_each_item_in_the_list_is_an_instance_of_the_Article_model(self) -> None:
        article = self.request.context["object"]
        self.assertTrue(isinstance(article, Article))
