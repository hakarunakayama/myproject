from django.contrib import admin
from .models.siteimage import SiteImage

@admin.register(SiteImage)
class SiteImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    search_fields = ('id', 'title')

# Register your models here.
