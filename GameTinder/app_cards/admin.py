from django.contrib import admin

from app_cards import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_id', 'name')