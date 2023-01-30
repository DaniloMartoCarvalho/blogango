"""Articles Model"""

from django.conf import settings
from django.db import models
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
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("author")
    )
    body = models.TextField(_("body"))
    status = models.CharField(
        _("status"), max_length=1, choices=Status.choices, default=Status.DRAFT
    )

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")
        ordering = ("title",)

    def __str__(self) -> str:
        return str(self.title)
