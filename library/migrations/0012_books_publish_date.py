# Generated by Django 4.1.7 on 2023-04-12 18:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0011_books_book_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="books",
            name="publish_date",
            field=models.IntegerField(
                default=2000,
                validators=[
                    django.core.validators.MaxValueValidator(3000),
                    django.core.validators.MinValueValidator(1000),
                ],
                verbose_name="تاریخ نشر",
            ),
            preserve_default=False,
        ),
    ]
