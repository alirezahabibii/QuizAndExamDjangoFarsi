from django.contrib import admin
from .models import Result


# Register your models here.
class ResultAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'user', 'score']
    list_filter = ['quiz', 'user']
    search_fields = ['quiz', 'user']


admin.site.register(Result, ResultAdmin)
