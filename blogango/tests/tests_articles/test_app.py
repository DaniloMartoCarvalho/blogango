from django.apps import apps


def tests_whether_the_article_app_is_installed_in_the_project():
    assert "articles" in apps.app_configs
