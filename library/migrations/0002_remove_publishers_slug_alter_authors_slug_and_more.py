# Generated by Django 4.1.7 on 2023-03-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="publishers",
            name="slug",
        ),
        migrations.AlterField(
            model_name="authors",
            name="slug",
            field=models.SlugField(default="", editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name="books",
            name="slug",
            field=models.SlugField(default="", editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name="genres",
            name="slug",
            field=models.SlugField(default="", editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name="translators",
            name="slug",
            field=models.SlugField(default="", editable=False, unique=True),
        ),
    ]