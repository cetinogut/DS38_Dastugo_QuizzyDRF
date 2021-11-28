from django.urls import path
from .views import Quiz , RandomQuestion, QuizQuestion

app_name='dastugo_quizzy_app'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz_list'),
    path('random/<str:topic>/', RandomQuestion.as_view(), name='random' ),
    path('question/<str:topic>/', QuizQuestion.as_view(), name='questions' ),
]