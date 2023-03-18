from django.contrib import admin

from library import models

admin.site.register(models.Authors)
admin.site.register(models.Books)
admin.site.register(models.Genres)
admin.site.register(models.Publishers)
admin.site.register(models.Translators)
