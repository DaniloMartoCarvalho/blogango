"""Core views"""

from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "pages/index.html"


index = IndexView.as_view()
