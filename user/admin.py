from django.contrib import admin
from .models import profile


@admin.register(profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'staff', 'address', 'phone']
    list_per_page = 50
    list_filter = ['staff']
    search_fields = ['staff']

