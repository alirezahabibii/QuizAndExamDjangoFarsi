from django.db import models


# Create your models here.

class ExamModel(models.Model):
    """
    Model for the exams.
    """
    name_cors = models.CharField(max_length=250, verbose_name='نام آزمون')
    date_exam = models.CharField(max_length=100, verbose_name='تاریخ آزمون')
    time_exam = models.CharField(max_length=100, verbose_name='ساعت آزمون')
    days_left = models.CharField(max_length=100, verbose_name='تعداد روز باقی مانده', blank=True, null=True, auto_created=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.name_cors

    class Meta:
        verbose_name = 'امتحان'
        verbose_name_plural = 'امتحانات'

    # # get the days left for the exam
    # def get_days_left(self):
    #     from datetime import datetime
    #     today = datetime.now()
    #     print(today)
    #     date_exam = datetime.strptime(self.date_exam, '%Y.%m.%d')
    #     days_left = (date_exam - today).days
    #     return days_left
    #
    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     self.days_left = self.get_days_left()
    #     super().save()
