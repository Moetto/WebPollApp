from django.contrib import admin
from ilmoapp.models import *
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin


class TextQuestionAdmin(PolymorphicChildModelAdmin):
    base_model = TextQuestion


class SelectOneQuestionAdmin(PolymorphicChildModelAdmin):
    base_model = SelectOneQuestion


class QuestionAdmin(PolymorphicParentModelAdmin):
    base_model = Question
    child_models = (
        (TextQuestion, TextQuestionAdmin),
        (SelectOneQuestion, SelectOneQuestionAdmin)
    )


admin.site.register(QuestionForm)
admin.site.register(TextQuestion, TextQuestionAdmin)
admin.site.register(Question, QuestionAdmin)