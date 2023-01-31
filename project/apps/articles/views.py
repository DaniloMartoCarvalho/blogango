""" View settings """

from django.views import generic

from .mixins import ArticleMixin


class ArticleList(ArticleMixin, generic.ListView):
    pass


articles_list = ArticleList.as_view()


class ArticleDetail(ArticleMixin, generic.DetailView):
    pass


articles_detail = ArticleDetail.as_view()
