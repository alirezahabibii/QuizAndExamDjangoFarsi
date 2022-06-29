from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User


# Create your models here.

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='سوالات')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', null=True, blank=True)
    score = models.FloatField(verbose_name='نمره')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'نتائج'
