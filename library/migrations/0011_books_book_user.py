# Generated by Django 4.1.7 on 2023-04-01 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("library", "0010_alter_authors_slug_alter_translators_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="books",
            name="book_user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="کاربر",
            ),
        ),
    ]
