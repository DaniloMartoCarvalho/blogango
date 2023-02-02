from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


class TestArticleListView:
    def tests_the_request_status_code(self, client):
        request = client.get(reverse("articles:article_list"))
        assert request.status_code == 200

    def tests_the_name_of_the_template_used_to_render_the_response(self, client):
        request = client.get(reverse("articles:article_list"))
        assertTemplateUsed(request, "articles/article_list.html")


class TestArticleDetailView:
    def tests_the_request_status_code(self, client):
        request = client.get(reverse("articles:article_detail", kwargs={"pk": 1}))
        assert request.status_code == 200

    def tests_the_name_of_the_template_used_to_render_the_response(self, client):
        request = client.get(reverse("articles:article_detail", kwargs={"pk": 1}))
        assertTemplateUsed(request, "articles/article_detail.html")
