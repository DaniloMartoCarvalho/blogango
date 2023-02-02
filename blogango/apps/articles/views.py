from django.views.generic import TemplateView


class ArticleList(TemplateView):
    template_name = "articles/article_list.html"


class ArticleDetail(TemplateView):
    template_name = "articles/article_detail.html"
