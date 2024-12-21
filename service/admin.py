from django.contrib import admin
from service.models import service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'Address')  # Ensure 'address' has the correct field name

admin.site.register(service, ServiceAdmin)

