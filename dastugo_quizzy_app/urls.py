from django.urls import path
from .views import Quiz , RandomQuestion, QuizQuestion, CategoryQuizzes, CategoryList

app_name='dastugo_quizzy_app'

urlpatterns = [
    #path('', CategoryList.as_view(), name="category-list"),
    path('', Quiz.as_view(), name='quiz-list'),
    path('quizzes/', Quiz.as_view(), name='quiz-list'),
    path("<category>/", CategoryQuizzes.as_view(), name="category-quizzes"),
    #path("<int:pk>/", CategoryQuizzes.as_view(), name="category-quizzes"),
    path('random/<str:topic>/', RandomQuestion.as_view(), name='random' ),
    path('question/<str:topic>/', QuizQuestion.as_view(), name='questions' ),
]