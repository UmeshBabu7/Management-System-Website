

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='instructors/')
    bio = models.TextField()
    experience = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    syllabus = models.TextField()
    duration = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    prerequisites = models.TextField(blank=True)
    enrollment_deadline = models.DateField()

    def __str__(self):
        return self.title

