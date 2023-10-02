from django.contrib import admin

# Register your models here.
from .models import Setting, ContactMessage, FAQ


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'create_at']
    list_filter = ['name', 'status', 'create_at']
    readonly_fields = ('name', 'email', 'subject', 'message', 'ip', 'create_at')




admin.site.register(Setting)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(FAQ)
