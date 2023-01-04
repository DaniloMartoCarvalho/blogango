from django.views import generic


class ArticleListView(generic.TemplateView):
    template_name = "article/article_list.html"


class ArticleDetailView(generic.TemplateView):
    template_name = "article/article_detail.html"
