from django.contrib import admin
from .models import School, InventoryItem, Request

admin.site.register(School)
admin.site.register(InventoryItem)
admin.site.register(Request)