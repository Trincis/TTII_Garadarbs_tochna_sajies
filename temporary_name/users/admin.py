from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from auditlog.models import LogEntry

# Remove or comment out this line
# admin.site.unregister(LogEntry)

admin.site.register(User, UserAdmin)

# Optional: Only register if not already registered, otherwise skip or customize
# @admin.register(LogEntry)
# class CustomLogEntryAdmin(admin.ModelAdmin):
#     list_display = ('object_repr', 'action', 'timestamp', 'actor')
#     list_filter = ('action', 'timestamp', 'actor')
