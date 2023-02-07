from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from taggit.models import Tag

from .models import Article


class ArticleMixin:
    queryset = Article.objects.published()


class BaseArticleListView(ArticleMixin, ListView):
    pass


class BaseArticleDetailView(ArticleMixin, DetailView):
    pass


class TagMixin:
    tag = None

    def get_tag(self):
        if not self.tag:
            tag_slug = self.kwargs.get("tag_slug")
            self.tag = get_object_or_404(Tag, slug=tag_slug) if tag_slug else None

        return self.tag

    def get_context_data(self, **kwargs):
        if "tag" not in kwargs:
            kwargs["tag"] = self.get_tag()
        return super().get_context_data(**kwargs)
