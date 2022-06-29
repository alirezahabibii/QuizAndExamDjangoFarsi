from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import View
from .models import ExamModel
from utils import get_date
from datetime import datetime


# Create your views here.

class ExamDatesView(View):
    def get(self, request: HttpRequest):
        exams: ExamModel = ExamModel.objects.filter(is_active=True).order_by('date_exam')
        today = datetime.strptime(get_date.iran_time(), '%Y-%m-%d')

        def delete_exam(exam: ExamModel):
            exam.is_active = False
            exam.save()

        def get_days_left(exam: ExamModel):
            date_exam = datetime.strptime(exam.date_exam, '%Y.%m.%d')
            days_left = (date_exam - today).days
            if days_left == 0:
                days_left = 'روز امتحان'
            elif days_left > 0:
                days_left = '( {} ) روز دیگه'.format(days_left)
            elif days_left < 0:
                delete_exam(exam)

            return days_left

        def save_days_left(exam: ExamModel):
            exam.days_left = get_days_left(exam)
            exam.save()

        for exam in exams:
            save_days_left(exam)

        exams_model: ExamModel = ExamModel.objects.filter(is_active=True).order_by('date_exam')

        context = {
            'exams': exams_model
        }
        return render(request, 'exam_dates/exam.html', context)

    def post(self, request: HttpRequest):
        pass
