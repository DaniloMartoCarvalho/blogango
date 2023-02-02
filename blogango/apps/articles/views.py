from django.shortcuts import get_object_or_404

from .mixins import BaseArticleDetailView, BaseArticleListView, TagMixin


class ArticleList(TagMixin, BaseArticleListView):
    paginate_by = 10

    def get_queryset(self):
        self.tag = self.get_tag()
        queryset = super().get_queryset()

        if self.tag:
            queryset = queryset.filter(tags__in=[self.tag])

        return queryset


class ArticleDetail(TagMixin, BaseArticleDetailView):
    def get_object(self):
        self.object = get_object_or_404(
            self.queryset,
            published__year=self.kwargs.get("year"),
            published__month=self.kwargs.get("month"),
            published__day=self.kwargs.get("day"),
            slug=self.kwargs.get("article_slug"),
        )

        return self.object
