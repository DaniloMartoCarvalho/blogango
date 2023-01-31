""" View settings """

from django.shortcuts import get_object_or_404
from django.views import generic

from .mixins import ArticleMixin
from .models import Article


class ArticleList(ArticleMixin, generic.ListView):
    paginate_by = 10


articles_list = ArticleList.as_view()


class ArticleDetail(ArticleMixin, generic.DetailView):
    def get_object(self) -> Article:
        self.object = get_object_or_404(
            self.get_queryset(),
            published__year=self.kwargs.get("year"),
            published__month=self.kwargs.get("month"),
            published__day=self.kwargs.get("day"),
            slug=self.kwargs.get("article_slug"),
        )

        return self.object


articles_detail = ArticleDetail.as_view()
