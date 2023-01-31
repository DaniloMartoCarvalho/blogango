""" View settings """

from django.views import generic


class ArticleList(generic.TemplateView):
    """
    Points the template to the URL that will list all the articles
    """

    template_name = "articles/articles_list.html"


articles_list = ArticleList.as_view()


class ArticleDetail(generic.TemplateView):
    """
    Points the template to the URL that will display only one article
    """

    template_name = "articles/articles_detail.html"


articles_detail = ArticleDetail.as_view()
