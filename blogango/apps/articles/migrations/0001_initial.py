# Generated by Django 4.1.6 on 2023-02-02 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="title")),
                (
                    "slug",
                    models.SlugField(
                        max_length=250, unique_for_date="published", verbose_name="slug"
                    ),
                ),
                ("body", models.TextField(verbose_name="body")),
                (
                    "status",
                    models.CharField(
                        choices=[("0", "draft"), ("1", "published")],
                        default="0",
                        max_length=1,
                        verbose_name="status",
                    ),
                ),
                (
                    "published",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="published"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="author",
                    ),
                ),
            ],
            options={
                "verbose_name": "article",
                "verbose_name_plural": "articles",
                "ordering": ("-published",),
            },
        ),
        migrations.AddIndex(
            model_name="article",
            index=models.Index(
                fields=["-published"], name="articles_ar_publish_84008d_idx"
            ),
        ),
    ]
