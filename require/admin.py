from django.contrib import admin
from .models import Requirement
class RequirementAdmin(admin.ModelAdmin):
	pass
admin.site.register(Requirement,RequirementAdmin)