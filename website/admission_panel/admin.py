from django.contrib import admin
from .models import AdminUser, FinancialReport

@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')
    

@admin.register(FinancialReport)
class FinancialReportAdmin(admin.ModelAdmin):
    list_display = ('total_revenue', 'report_date')
    
