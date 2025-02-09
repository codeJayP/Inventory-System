from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Equipment)
class userData(ImportExportModelAdmin):
    pass
# Register your models here.
class EquipementAdmin(admin.ModelAdmin):
    list_display = ['property_num', 'article_item', 'description', 'person_accountable', 'cost']
    search_fields = ['property_num', 'article_item', 'description', 'person_accountable', 'cost']
# admin.site.register(Equipment, EquipementAdmin)