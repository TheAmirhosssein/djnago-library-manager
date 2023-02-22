from django.db import models

PROFESSIONS = (
    ("نویسنده", "AUTHOR"),
    ("ویراستار", "EDITOR"),
    ("نویسنده", "TRANSLATOR"),
)


class Authors(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    profession = models.CharField(
        choices=PROFESSIONS, max_length=3, verbose_name="حرفه"
    )
    heigh = models.CharField(max_length=10, verbose_name="قد")
    birth_date = models.CharField(max_length=50, verbose_name="تاریخ تولد")
    birth_place = models.CharField(max_length=50, verbose_name="محل تولد")
