from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "published")
    ordering = ("status", "published")
    search_fields = ("title", "author")
    raw_id_fields = ("author",)
    date_hierarchy = "published"
    exclude = ("slug",)
