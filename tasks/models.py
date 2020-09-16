from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    due_date = models.DateField()

    def __str__(self):
        return f'{self.task} - {self.due_date}'
