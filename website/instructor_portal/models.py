

from django.db import models

class InstructorProfile(models.Model):
    instructor = models.OneToOneField('courses.Instructor', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.instructor

class AssignmentGrade(models.Model):
    assignment = models.ForeignKey('student_portal.Assignment', on_delete=models.CASCADE)
    instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.assignment} - {self.grade}"
