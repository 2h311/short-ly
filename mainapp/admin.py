from django.contrib import admin

from .models import ShortLinks

# Register your models here.
@admin.register(ShortLinks)
class ShortyAdmin(admin.ModelAdmin):
	list_display = ('id', 'short_link', 'full_link')