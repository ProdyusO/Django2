from django.contrib import admin

from .models import Exam, Choice, Question, Result

admin.site.register(Exam)
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Result)