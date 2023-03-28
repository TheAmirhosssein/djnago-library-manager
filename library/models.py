from django.db import models
from django.utils.text import slugify


class Authors(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    slug = models.SlugField(
        max_length=20, allow_unicode=True, unique=True, editable=False
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Translators(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    slug = models.SlugField(
        max_length=20, allow_unicode=True, unique=True, editable=False
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Genres(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(
        max_length=20, allow_unicode=True, unique=True, editable=False
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Publishers(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    website = models.URLField(verbose_name="وب سایت")

    def __str__(self):
        return self.title


class Books(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(
        max_length=20, allow_unicode=True, unique=True, editable=False
    )
    translator = models.ForeignKey(
        Translators,
        verbose_name="مترجم",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        Authors, verbose_name="نویسنده", on_delete=models.CASCADE
    )
    genres = models.ManyToManyField(Genres, verbose_name="ژانر")
    publisher = models.ForeignKey(
        Publishers, verbose_name="ناشر", on_delete=models.CASCADE
    )
    book_image = models.ImageField(upload_to="images/books", verbose_name="کاور کتاب")
    detail = models.TextField(verbose_name="توضیحات")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title} | {self.author}"
