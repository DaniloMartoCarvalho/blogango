""" URLs settings """

from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path("", views.articles_list, name="list"),
    path(
        "article/<int:year>/<int:month>/<int:day>/<slug:article_slug>/",
        views.articles_detail,
        name="detail",
    ),
]
