from django.contrib import admin
from .models import Quiz


# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_questions', 'time', 'equired_score_to_pass', 'difficluty')
    search_fields = ('name', 'time')
    list_filter = ('difficluty',)


admin.site.register(Quiz, QuizAdmin)
