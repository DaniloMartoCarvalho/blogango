from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status")
    list_filter = ("status", "created", "modified")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    ordering = ("status",)
