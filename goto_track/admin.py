from django.contrib import admin
from models import Click

class ClickAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'content_type', 'referer', 'user', 'date')
    list_display_links = ('content_object',)
    list_filter = ('date', 'referer','user')

admin.site.register(Click, ClickAdmin)
