from django.test import TestCase
from django.urls import reverse


class ArticleListViewTestCase(TestCase):
    def setUp(self) -> None:
        self.request = self.client.get(reverse("articles:list"))

    def test_the_request_status_code(self) -> None:
        self.assertEqual(self.request.status_code, 200)

    def test_the_name_of_the_template_used_to_render_the_response(self) -> None:
        self.assertTemplateUsed(self.request, "articles/articles_list.html")


class ArticleDetailViewTestCase(TestCase):
    def setUp(self) -> None:
        datas = {
            "pk": 1,
        }
        self.request = self.client.get(reverse("articles:detail", kwargs=datas))

    def test_the_request_status_code(self) -> None:
        self.assertEqual(self.request.status_code, 200)

    def test_the_name_of_the_template_used_to_render_the_response(self) -> None:
        self.assertTemplateUsed(self.request, "articles/articles_detail.html")
