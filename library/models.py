from django.db import models
from django.template.defaultfilters import slugify


class Authors(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    slug = models.SlugField(db_index=True, null=False, default="", unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return super().__str__(self.name)


class Translators(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    slug = models.SlugField(db_index=True, null=False, default="", unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return super().__str__(self.name)


class Genres(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(db_index=True, null=False, default="", unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return super().__str__(self.title)


class Publishers(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    website = models.URLField(verbose_name="وب سایت")
    slug = models.SlugField(db_index=True, null=False, default="", unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return super().__str__(self.title)
