from django.views.generic import DetailView, ListView

from .mixins import ArticleMixin


class ArticleList(ArticleMixin, ListView):
    paginate_by = 10


class ArticleDetail(ArticleMixin, DetailView):
    pass
