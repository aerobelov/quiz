from django.contrib import admin

# Register your models here.

from .models import Question_set, Question_type, Question, Answer_option, Answer_option, Answer, QuizParticipant

admin.site.register(Question)
admin.site.register(Question_set)
admin.site.register(Question_type)
admin.site.register(Answer_option)
admin.site.register(Answer)
admin.site.register(QuizParticipant)

