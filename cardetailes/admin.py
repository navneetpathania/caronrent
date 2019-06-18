from django.contrib import admin
from .models import CarDetailes


class CarDetailesAdmin(admin.ModelAdmin):
    list_display = ("name","brand","image")


admin.site.register(CarDetailes,CarDetailesAdmin)


