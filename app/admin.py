from django.contrib import admin
from . import models
# Register your models here.


class ArteAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'autor')
    list_per_page = 10


admin.site.register(models.Poesia, ArteAdmin)
admin.site.register(models.Pintura, ArteAdmin)

