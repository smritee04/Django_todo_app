from django.db import models
from django.contrib.auth.models import User

class TODOAPP(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    task_name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name