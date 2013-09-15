from .models import friendlink
from django.contrib import admin
class friendlinkAdmin(admin.ModelAdmin):
    pass
admin.site.register(friendlink,friendlinkAdmin)

