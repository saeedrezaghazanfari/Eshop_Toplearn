from django.contrib import admin
from .models import contactus_model

class contactAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subject', 'is_read']
    list_filter = ['username']
    list_editable = ['is_read']
    search_fields = ['username']

admin.site.register(contactus_model, contactAdmin)