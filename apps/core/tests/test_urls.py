from django.test import SimpleTestCase
from django.urls import resolve, reverse

from .. import views as v


class TestIndexURL(SimpleTestCase):
    def setUp(self) -> None:
        self.url = reverse("core:index")

    def test_route_match(self) -> None:
        self.assertEqual(resolve(self.url).route, "")

    def test_func_view(self) -> None:
        self.assertEqual(resolve(self.url).func, v.index)
