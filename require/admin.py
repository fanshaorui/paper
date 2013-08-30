from django.contrib import admin
from .models import Requirement,Category
class RequirementAdmin(admin.ModelAdmin):
	pass
class CategoryAdmin(admin.ModelAdmin):
	pass
admin.site.register(Requirement,RequirementAdmin)
admin.site.register(Category,RequirementAdmin)