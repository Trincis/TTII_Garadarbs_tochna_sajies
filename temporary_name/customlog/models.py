from django.db import models

class AuditLog(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)  # string reference here
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action} at {self.timestamp}"
