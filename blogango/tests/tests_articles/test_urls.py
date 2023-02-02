import pytest
from apps.articles.views import ArticleDetail, ArticleList
from django.urls import resolve, reverse


@pytest.fixture
def article_list_match():
    return resolve(reverse("articles:article_list"))


@pytest.fixture
def article_list_by_tag_match():

    datas = {
        "tag_slug": "tag-test",
    }

    return resolve(reverse("articles:article_list_by_tag", kwargs=datas))


@pytest.fixture
def article_detail_match():

    datas = {
        "year": 2023,
        "month": 2,
        "day": 2,
        "article_slug": "test-slug",
    }

    return resolve(reverse("articles:article_detail", kwargs=datas))


@pytest.fixture
def article_detail_by_tag_match():

    datas = {
        "year": 2023,
        "month": 2,
        "day": 2,
        "article_slug": "test-slug",
        "tag_slug": "tag-test",
    }

    return resolve(reverse("articles:article_detail_by_tag", kwargs=datas))


class TestArticleListUrl:
    def tests_the_view_that_lists_the_articles(self, article_list_match):
        assert article_list_match.func.view_class == ArticleList

    def tests_the_parameter_list_of_the_url_matching_pattern(self, article_list_match):
        assert article_list_match.kwargs == {}

    def tests_the_url_matching_pattern(self, article_list_match):
        assert article_list_match.route == ""


class TestArticleListByTag:
    def tests_the_view_that_lists_the_articles(self, article_list_by_tag_match):
        assert article_list_by_tag_match.func.view_class == ArticleList

    def tests_the_parameter_list_of_the_url_matching_pattern(
        self, article_list_by_tag_match
    ):
        assert article_list_by_tag_match.kwargs == {
            "tag_slug": "tag-test",
        }

    def tests_the_url_matching_pattern(self, article_list_by_tag_match):
        assert article_list_by_tag_match.route == "tag/<slug:tag_slug>/"


class TestArticleDetailUrl:
    def tests_the_view_that_lists_the_articles(self, article_detail_match):
        assert article_detail_match.func.view_class == ArticleDetail

    def tests_the_parameter_list_of_the_url_matching_pattern(
        self, article_detail_match
    ):
        assert article_detail_match.kwargs == {
            "year": 2023,
            "month": 2,
            "day": 2,
            "article_slug": "test-slug",
        }

    def tests_the_url_matching_pattern(self, article_detail_match):
        assert (
            article_detail_match.route
            == "articles/<int:year>/<int:month>/<int:day>/<slug:article_slug>/"
        )


class TestArticleDetailByTagUrl:
    def tests_the_view_that_lists_the_articles(self, article_detail_by_tag_match):
        assert article_detail_by_tag_match.func.view_class == ArticleDetail

    def tests_the_parameter_list_of_the_url_by_tag_matching_pattern(
        self, article_detail_by_tag_match
    ):
        assert article_detail_by_tag_match.kwargs == {
            "year": 2023,
            "month": 2,
            "day": 2,
            "article_slug": "test-slug",
            "tag_slug": "tag-test",
        }

    def tests_the_url_by_tag_matching_pattern(self, article_detail_by_tag_match):
        assert article_detail_by_tag_match.route == (
            "tag/<slug:tag_slug>/"
            "articles/<int:year>/<int:month>/<int:day>/<slug:article_slug>/"
        )
