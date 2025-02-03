from django.contrib import admin
from .models import *
# Register your models here.
class EquipementAdmin(admin.ModelAdmin):
    list_display = ['property_num', 'article_item', 'description', 'person_accountable', 'cost']
    search_fields = ['property_num', 'article_item', 'description', 'person_accountable', 'cost']
admin.site.register(Equipment, EquipementAdmin)