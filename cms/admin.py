from .models import customerExample,writerExample
from django.contrib import admin
class writerExampleAdmin(admin.ModelAdmin):
    pass
class customerExampleAdmin(admin.ModelAdmin):
    pass
admin.site.register(customerExample,customerExampleAdmin)
admin.site.register(writerExample,writerExampleAdmin)

