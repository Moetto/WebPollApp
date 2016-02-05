from django.conf.urls import url
from ilmoapp.views import QuestionForm

urlpatterns = [
    url(r'^(?P<id>\d{1,2})$', QuestionForm.as_view()),
]