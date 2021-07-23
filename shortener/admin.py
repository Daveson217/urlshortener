from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    model = Link
    list_display = ['id', 'full_link', 'short_link']
    #list_filter = ('block',)
    add_fieldsets = [ 'full_link', 'short_link']
    ordering = ['id']

admin.site.register(Link, LinkAdmin)