from django.db import models
from django.template.defaultfilters import slugify

PROFESSIONS = (
    ("نویسنده", "AUTHOR"),
    ("ویراستار", "EDITOR"),
    ("منرجم", "TRANSLATOR"),
)


class Authors(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    profession = models.CharField(
        choices=PROFESSIONS, max_length=3, verbose_name="حرفه"
    )
    slug = models.SlugField(db_index=True, null=False, default="", unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return super().__str__(self.name)

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"
