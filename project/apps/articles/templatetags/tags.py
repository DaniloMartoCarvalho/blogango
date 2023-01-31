from django import template
from taggit.models import Tag

register = template.Library()


@register.inclusion_tag("includes/tags.html")
def tags() -> dict:
    return {
        "tags": Tag.objects.all(),
    }
