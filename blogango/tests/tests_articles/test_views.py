import pytest
from apps.articles.models import Article
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from ..factories.articles import ArticleFactory

pytestmark = pytest.mark.django_db


class TestArticleListView:
    def tests_the_request_status_code(self, client):
        request = client.get(reverse("articles:article_list"))
        assert request.status_code == 200

    def tests_the_name_of_the_template_used_to_render_the_response(self, client):
        request = client.get(reverse("articles:article_list"))
        assertTemplateUsed(request, "articles/article_list.html")

    def tests_if_articles_are_being_listed(self, client):
        ArticleFactory(status=Article.Status.PUBLISHED)
        request = client.get(reverse("articles:article_list"))
        assert len(request.context["object_list"]) == 1

    def tests_whether_only_articles_with_published_status_are_listed(self, client):
        ArticleFactory(status=Article.Status.PUBLISHED)
        ArticleFactory(status=Article.Status.DRAFT)
        request = client.get(reverse("articles:article_list"))
        assert len(request.context["object_list"]) == 1

    def tests_the_articles_listed_are_instances_of_the_article_model(self, client):
        ArticleFactory(status=Article.Status.PUBLISHED)
        request = client.get(reverse("articles:article_list"))
        article = request.context["object_list"][0]
        assert isinstance(article, Article)


class TestArticleListPagination:
    def tests_if_the_listing_of_articles_is_not_paginated_when_there_are_less_than_10_articles(
        self, client
    ):
        request = client.get(reverse("articles:article_list"))
        assert not request.context["is_paginated"]

    def tests_whether_the_listing_is_paginated_when_there_are_more_than_10_articles(
        self, client
    ):

        for _ in range(15):
            ArticleFactory(status=Article.Status.PUBLISHED)

        request = client.get(reverse("articles:article_list"))
        assert request.context["is_paginated"]

    def tests_if_10_articles_are_listed_by_pages(self, client):
        for _ in range(15):
            ArticleFactory(status=Article.Status.PUBLISHED)

        request = client.get(reverse("articles:article_list"))
        assert len(request.context["object_list"]) == 10

    def tests_if_all_articles_are_listed(self, client):
        for _ in range(15):
            ArticleFactory(status=Article.Status.PUBLISHED)

        request = client.get(f"{reverse('articles:article_list')}?page=2")
        assert len(request.context["object_list"]) == 5


class TestArticleDetailView:
    def tests_the_status_code_when_the_article_has_no_published_status(self, client):
        article = ArticleFactory(status=Article.Status.DRAFT)
        request = client.get(article.get_absolute_url())
        assert request.status_code == 404

    def tests_the_request_status_code(self, client):
        article = ArticleFactory(status=Article.Status.PUBLISHED)
        request = client.get(article.get_absolute_url())
        assert request.status_code == 200

    def tests_the_name_of_the_template_used_to_render_the_response(self, client):
        article = ArticleFactory(status=Article.Status.PUBLISHED)
        request = client.get(article.get_absolute_url())
        assertTemplateUsed(request, "articles/article_detail.html")

    def testa_of_the_searched_articles_is_an_instance_of_the_article_model(
        self, client
    ):
        article = ArticleFactory(status=Article.Status.PUBLISHED)
        request = client.get(article.get_absolute_url())
        article = request.context["object"]
        assert isinstance(article, Article)
