from django.contrib import admin
from .models import AuditLog

class AuditLogAdmin(admin.ModelAdmin):
    pass

# Try to register, ignore if already registered
try:
    admin.site.register(AuditLog, AuditLogAdmin)
except admin.sites.AlreadyRegistered:
    pass
