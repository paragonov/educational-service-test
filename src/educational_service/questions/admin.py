from django.contrib import admin

from educational_service.questions.models import Theme, Answer, Question, TestCase, TestCaseResults


admin.site.register(Theme)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(TestCase)
admin.site.register(TestCaseResults)
