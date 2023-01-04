from django.test import SimpleTestCase
from django.urls import resolve, reverse

from .. import views


class TestArticleListUrl(SimpleTestCase):
    def setUp(self) -> None:
        self.match = resolve(reverse("articles:article_list"))

    def test_the_view_function_that_would_be_used_to_serve_the_URL(self) -> None:
        self.assertEqual(self.match.func.view_class, views.ArticleListView)

    def test_the_route_of_the_matching_URL_pattern(self) -> None:
        self.assertEqual(self.match.route, "")


class TestArticleDetailUrl(SimpleTestCase):
    def setUp(self) -> None:
        self.match = resolve(reverse("articles:article_detail", kwargs={"pk": 1}))

    def test_the_view_function_that_would_be_used_to_serve_the_URL(self) -> None:
        self.assertEqual(self.match.func.view_class, views.ArticleDetailView)

    def test_the_route_of_the_matching_URL_pattern(self) -> None:
        self.assertEqual(self.match.route, "<int:pk>/")
