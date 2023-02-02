from apps.articles.views import ArticleDetail, ArticleList
from django.urls import resolve, reverse


class TestArticleListUrl:
    def tests_the_view_that_lists_the_articles(self):
        match = resolve(reverse("articles:article_list"))
        assert match.func.view_class == ArticleList

    def tests_the_parameter_list_of_the_url_matching_pattern(self):
        match = resolve(reverse("articles:article_list"))
        assert match.kwargs == {}

    def tests_the_url_matching_pattern(self):
        match = resolve(reverse("articles:article_list"))
        assert match.route == ""


class TestArticleDetailUrl:
    def tests_the_view_that_lists_the_articles(self):
        match = resolve(reverse("articles:article_detail", kwargs={"pk": 1}))
        assert match.func.view_class == ArticleDetail

    def tests_the_parameter_list_of_the_url_matching_pattern(self):
        match = resolve(reverse("articles:article_detail", kwargs={"pk": 1}))
        assert match.kwargs == {"pk": 1}

    def tests_the_url_matching_pattern(self):
        match = resolve(reverse("articles:article_detail", kwargs={"pk": 1}))
        assert match.route == "articles/<int:pk>/"
