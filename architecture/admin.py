from django.contrib import admin
from .models import Architecture, Architect, Country, Structure
# Register your models here.


@admin.register(Architecture)
class ArchitectureAdmin(admin.ModelAdmin):
    ordering = ("id",)


@admin.register(Architect)
class ArchitectAdmin(admin.ModelAdmin):
    ordering = ("id",)


admin.site.register([Country, Structure])
