from django.contrib import admin
from exam_dates.models import ExamModel


# Register your models here.

class ExamAdmin(admin.ModelAdmin):
    list_display = ['name_cors', 'date_exam', 'time_exam', 'days_left', 'is_active']
    list_filter = ['name_cors', 'is_active', 'date_exam']


admin.site.register(ExamModel, ExamAdmin)
