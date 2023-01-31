"""Articles Model"""

from typing import Self

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext as _


class TimeStampedModel(models.Model):
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        abstract = True


class Article(TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = 0, _("draft")
        PUBLISHED_AND_AVAILABLE = 1, _("published and available")
        PUBLISHED_AND_UNVAILABLE = 2, _("published and unavailable")

    title = models.CharField(_("title"), max_length=250)
    slug = models.SlugField(_("slug"), max_length=250, unique_for_date="published")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("author")
    )
    body = models.TextField(_("body"))
    status = models.CharField(
        _("status"), max_length=1, choices=Status.choices, default=Status.DRAFT
    )

    published = models.DateTimeField(_("published"), default=timezone.now)

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")
        ordering = ("-published",)

        indexes = [models.Index(fields=["-published"])]

    def __str__(self) -> str:
        return str(self.title)

    def save(self, *args, **kwargs) -> Self:
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        datas = {
            "year": self.published.year,
            "month": self.published.month,
            "day": self.published.day,
            "article_slug": self.slug,
        }

        return reverse("articles:detail", kwargs=datas)
