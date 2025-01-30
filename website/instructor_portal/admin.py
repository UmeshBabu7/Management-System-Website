from django.contrib import admin
from .models import InstructorProfile, AssignmentGrade

@admin.register(InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
    list_display = ('instructor',)
   

@admin.register(AssignmentGrade)
class AssignmentGradeAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'instructor', 'grade')
  
