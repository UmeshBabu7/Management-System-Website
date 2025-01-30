

from django.db import models

class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    purpose = models.CharField(max_length=50, choices=[('Course Inquiry', 'Course Inquiry'), ('Technical Support', 'Technical Support')])

    def __str__(self):
        return f"{self.name} - {self.purpose}"
