from django.db import models
from users.models import CustomUser
from projects.models import Task

class TimeLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField()
    hours_spent = models.DecimalField(max_digits=4, decimal_places=2)