

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    application_deadline = models.DateField()

    def __str__(self):
        return self.title

class Alumni(models.Model):
    name = models.CharField(max_length=255)
    success_story = models.TextField()

    def __str__(self):
        return self.name
