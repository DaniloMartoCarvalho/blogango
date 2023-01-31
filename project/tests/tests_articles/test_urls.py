from apps.articles.views import articles_detail, articles_list
from django.test import SimpleTestCase
from django.urls import resolve, reverse


class ArticlesListUrlTestCase(SimpleTestCase):
    def setUp(self) -> None:
        self.match = resolve(reverse("articles:list"))

    def test_the_view_function_that_would_be_used_to_serve_the_URL(self) -> None:
        self.assertEqual(self.match.func, articles_list)

    def test_the_route_of_the_matching_URL_pattern(self) -> None:
        self.assertEqual(self.match.route, "")


class ArticleDetailUrlTestCase(SimpleTestCase):
    def setUp(self) -> None:
        datas = {
            "pk": 1,
        }
        self.match = resolve(reverse("articles:detail", kwargs=datas))

    def test_the_view_function_that_would_be_used_to_serve_the_URL(self) -> None:
        self.assertEqual(self.match.func, articles_detail)

    def test_all_keyword_arguments_that_would_be_passed_to_the_view_function(
        self,
    ) -> None:
        self.assertEqual(self.match.kwargs, {"pk": 1})

    def test_the_route_of_the_matching_URL_pattern(self) -> None:
        self.assertEqual(self.match.route, "article/<int:pk>/")
