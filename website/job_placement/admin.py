from django.contrib import admin
from .models import Job, Alumni

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'application_deadline')
  

@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('name',)
   
