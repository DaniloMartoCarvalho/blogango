from django.views import generic

from .models import Article


class ArticleMixin:
    def get_queryset(self):
        return Article.objects.published()


class ArticleListView(ArticleMixin, generic.ListView):
    template_name = "article/article_list.html"


class ArticleDetailView(ArticleMixin, generic.DetailView):
    template_name = "article/article_detail.html"
