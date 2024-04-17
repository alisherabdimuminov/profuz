from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Job


@admin.register(Job)
class JobModelAdmin(ModelAdmin):
    list_display = ['title', 'category', 'price']