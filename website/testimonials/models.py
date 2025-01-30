from django.db import models

class Testimonial(models.Model):
    student_name = models.CharField(max_length=255)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    feedback = models.TextField()
    video_link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.course}"

class Review(models.Model):
    student = models.CharField(max_length=255)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()

    def __str__(self):
        return f"{self.student} - {self.course} ({self.rating} stars)"
