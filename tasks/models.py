import uuid

from django.db import models


# Create your models here.
class Tasks(models.Model):
    taskText = models.TextField()
    taskStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.taskText
