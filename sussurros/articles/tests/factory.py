import factory
from django.contrib.auth import get_user_model
from factory import django, fuzzy

from ..models import Article

User = get_user_model()


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    username = fuzzy.FuzzyText()
    password = fuzzy.FuzzyText()


class ArticleFactory(django.DjangoModelFactory):
    class Meta:
        model = Article

    title = fuzzy.FuzzyText()
    author = factory.SubFactory(UserFactory)
    body = fuzzy.FuzzyText()
    status = fuzzy.FuzzyChoice([Article.Status.DRAFT, Article.Status.PUBLISHED])
