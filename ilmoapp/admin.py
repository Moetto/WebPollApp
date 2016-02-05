from collections import OrderedDict

from io import StringIO, BytesIO
from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse
from xlsxwriter.workbook import Workbook
from ilmoapp.models import *
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin


def download_replies(modeladmin, request, queryset):
    output = BytesIO()
    workbook = Workbook(output, {'in_memory': True})
    sheet = workbook.add_worksheet('test')

    question_columns = OrderedDict()
    max_column = 0
    row = 1
    for reply in queryset:
        for question in reply.answers.keys():
            current_column = question_columns.get(question, max_column)
            if current_column == max_column:
                question_columns[question] = max_column
                max_column += 1
            sheet.write(row, current_column, reply.answers[question])
        row += 1

    responses = {}
    for reply in queryset:
        for question in reply.answers.keys():
            if responses.get(question) is None:
                responses[question] = []
            responses[question].append(reply.answers[question])
    for question in question_columns.keys():
        sheet.write(0, question_columns[question], question)

    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=test.xlsx"
    return response


def download_questionnaire_replies(modeladmin, request, queryset):
    pass


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
    actions = [download_questionnaire_replies]


class ReplyAdmin(admin.ModelAdmin):
    actions = [download_replies]


admin.site.register(Reply, ReplyAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(TextQuestion, TextQuestionAdmin)
admin.site.register(Question, QuestionAdmin)
