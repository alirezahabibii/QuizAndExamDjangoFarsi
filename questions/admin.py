from django.contrib import admin
from .models import Question, Answer


# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['text', 'quiz', 'created']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'correct', 'question')
    search_fields = ('text',)
    list_filter = ('correct',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
