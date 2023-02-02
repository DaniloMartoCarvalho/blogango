from .models import Article


class ArticleMixin:
    queryset = Article.objects.published()
