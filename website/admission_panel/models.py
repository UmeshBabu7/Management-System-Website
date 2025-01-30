
from django.db import models

class AdminUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('Manager', 'Manager')])

    def __str__(self):
        return f"{self.username} ({self.role})"

class FinancialReport(models.Model):
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2)
    report_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Report - {self.report_date}"
