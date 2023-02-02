from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel


class ArticleManager(models.Manager):
    def published(self):
        queryset = super().get_queryset().defer("created", "modified")
        return queryset.filter(status=self.model.Status.PUBLISHED)


class Article(TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = 0, _("draft")
        PUBLISHED = 1, _("published")

    title = models.CharField(_("title"), max_length=250)
    slug = models.SlugField(_("slug"), max_length=250, unique_for_date="published")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("author"),
    )
    body = models.TextField(_("body"))
    status = models.CharField(
        _("status"), max_length=1, choices=Status.choices, default=Status.DRAFT
    )

    published = models.DateTimeField(_("published"), default=timezone.now)

    objects = ArticleManager()

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")
        ordering = ("-published",)

        indexes = [models.Index(fields=["-published"])]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        datas = {
            "year": self.published.year,
            "month": self.published.month,
            "day": self.published.day,
            "article_slug": self.slug,
        }

        return reverse("articles:article_detail", kwargs=datas)
