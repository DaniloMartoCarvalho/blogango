from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .mixins import ArticleMixin


class ArticleList(ArticleMixin, ListView):
    paginate_by = 10


class ArticleDetail(ArticleMixin, DetailView):
    def get_object(self):
        self.object = get_object_or_404(
            self.queryset,
            published__year=self.kwargs.get("year"),
            published__month=self.kwargs.get("month"),
            published__day=self.kwargs.get("day"),
            slug=self.kwargs.get("article_slug"),
        )

        return self.object
