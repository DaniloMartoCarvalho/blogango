from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path(
        "",
        views.ArticleList.as_view(),
        name="article_list",
    ),
    path(
        "articles/<int:year>/<int:month>/<int:day>/<slug:article_slug>/",
        views.ArticleDetail.as_view(),
        name="article_detail",
    ),
]
