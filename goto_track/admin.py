from django.contrib import admin
from models import Click

class ClickAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'referer', 'user', 'date')    
    list_display_links = ('content_object',)

admin.site.register(Click, ClickAdmin)
