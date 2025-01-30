

from django.db import models

class StudentProfile(models.Model):
    student = models.OneToOneField('admissions.Student', on_delete=models.CASCADE)
    enrolled_courses = models.ManyToManyField('courses.Course')
    
    def __str__(self):
        return self.student

class Progress(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    progress_percentage = models.FloatField(default=0)

    def __str__(self):
        return f"{self.student.student} - {self.course} ({self.progress_percentage}%)"

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    submitted_file = models.FileField(upload_to='assignments/')
    submitted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.student} - {self.title}"
