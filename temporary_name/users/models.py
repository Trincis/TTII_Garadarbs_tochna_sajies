from django.contrib.auth.models import AbstractUser
from django.db import models
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField

class Role(models.Model):
    name = models.CharField(max_length=50)
    history = AuditlogHistoryField()

    def __str__(self):
        return self.name

auditlog.register(Role)

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
