from django.db import models


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ToDoHistory(models.Model):
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE)
    EVENT_CHOICES = [
        ('Created', 'Created'),
        ('Updated', 'Updated'),
        ('Checked', 'Checked'),
        ('Unchecked', 'Unchecked'),
        ('Deleted', 'Deleted'),
    ]

    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    timestamp = models.DateTimeField()
    details = models.TextField()





