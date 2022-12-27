from django.test import SimpleTestCase
from django.urls import reverse


class TestIndexView(SimpleTestCase):
    def test_template_used_by_index_view(self) -> None:
        request = self.client.get(reverse("core:index"))
        self.assertTemplateUsed(request, "pages/index.html")
