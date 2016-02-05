from django.contrib import admin
from ilmoapp.models import *
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin


class TextQuestionAdmin(PolymorphicChildModelAdmin):
    base_model = TextQuestion
    exclude = ['answer']


class SelectOneQuestionAdmin(PolymorphicChildModelAdmin):
    base_model = SelectOneQuestion


class TextQuestionInline(admin.StackedInline):
    model = TextQuestion
    readonly_fields = ['question_ptr']
    exclude = ['answer']


class QuestionAdmin(PolymorphicParentModelAdmin):
    base_model = Question
    child_models = (
        (TextQuestion, TextQuestionAdmin),
        (SelectOneQuestion, SelectOneQuestionAdmin)
    )


class QuestionnaireAdmin(admin.ModelAdmin):
    inlines = [TextQuestionInline]


admin.site.register(Reply)
admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(TextQuestion, TextQuestionAdmin)
admin.site.register(Question, QuestionAdmin)
