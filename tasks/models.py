from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    task = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    due_date = models.DateField()
    tags = models.ManyToManyField(Tag, related_name='tasks', blank=True, default='')

    def __str__(self):
        return f'{self.task} - {self.due_date}'
