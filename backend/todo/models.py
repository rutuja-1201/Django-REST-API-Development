from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status_choices = [('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')]
    status = models.CharField(max_length=20, choices=status_choices)
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
