from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Resume


@admin.register(Resume)
class ResumeModelAdmin(ModelAdmin):
    list_display = ["first_name", "last_name", "email"]
