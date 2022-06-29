from django.db import models
from quizes.models import Quiz


# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=200, verbose_name='متن سوال')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='آزمون')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name_plural = 'سوالات'


class Answer(models.Model):
    text = models.CharField(max_length=200, verbose_name='پاسخ متن ')
    correct = models.BooleanField(default=False, verbose_name='پاسخ صحت ')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='سوال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f'question: {self.question.text} - answer: {self.text}, correct: {self.correct}'

    def get_question(self):
        pass

    class Meta:
        verbose_name_plural = 'پاسخ ها'
