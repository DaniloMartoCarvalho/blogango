import pytest
from apps.articles.models import Article
from django.urls import reverse
from django.utils.text import slugify

from ..factories.articles import ArticleFactory

pytestmark = pytest.mark.django_db


class TestArticleModel:
    def tests_whether_an_article_is_saved_to_the_bank_when_it_is_created(self):
        ArticleFactory()
        assert Article.objects.count() == 1

    def test_the_slug_is_obtained_from_the_title(self):
        article = ArticleFactory()
        slug = slugify(article.title)
        assert article.slug == slug

    def test_the_absolute_URL_of_an_article(self):
        article = ArticleFactory()

        datas = {
            "pk": article.pk,
        }

        url = reverse("articles:article_detail", kwargs=datas)
        assert article.get_absolute_url() == url
