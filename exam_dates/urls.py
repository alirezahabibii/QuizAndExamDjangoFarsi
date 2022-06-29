from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExamDatesView.as_view(), name='exam_dates'),
]
