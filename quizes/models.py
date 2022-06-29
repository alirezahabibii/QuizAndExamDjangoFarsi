from django.db import models
import random

# Create your models here.
DIFF_CHOICES = (('آسان', 'آسان'), ('متوسط', 'متوسط'), ('سخت', 'سخت'))


class Quiz(models.Model):
    name = models.CharField(max_length=120, verbose_name='نام آزمون')
    topic = models.CharField(max_length=120, verbose_name='موضوع')
    number_of_questions = models.IntegerField(default=0, verbose_name='تعداد سوالات')
    time = models.IntegerField(help_text='duration of the quiz in minutes', verbose_name='زمان آزمون')
    equired_score_to_pass = models.IntegerField(help_text='required score in %', verbose_name='نمره مورد نیاز')
    difficluty = models.CharField(max_length=120, choices=DIFF_CHOICES, verbose_name='سطح آزمون')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return f'{self.name} - {self.topic}'

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'آزمون ها'
