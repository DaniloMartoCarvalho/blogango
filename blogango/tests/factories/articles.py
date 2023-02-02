import factory
from apps.articles.models import Article
from django.contrib.auth import get_user_model
from factory import django, fuzzy


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = fuzzy.FuzzyText()
    password = fuzzy.FuzzyText()


class ArticleFactory(django.DjangoModelFactory):
    class Meta:
        model = Article

    title = fuzzy.FuzzyText()
    author = factory.SubFactory(UserFactory)
    body = fuzzy.FuzzyText()
    status = fuzzy.FuzzyChoice(
        [
            Article.Status.DRAFT,
            Article.Status.PUBLISHED,
        ]
    )
