from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzy, Question, Category
from .serializers import QuizzySerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView

class Quiz(generics.ListAPIView): # list all quizzes
    serializer_class = QuizzySerializer
    queryset = Quizzy.objects.all()

class RandomQuestion(APIView): # APIView gives us more control
    def get(self, request, format=None, **kwargs):
        rand_question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1] # select a random question in a simple way based on title
        serializer = RandomQuestionSerializer(rand_question, many=True) # we may want to get more than one, multiple questions
        return Response(serializer.data)

class QuizQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        quiz_questions_on_topic = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz_questions_on_topic, many=True)
        return Response(serializer.data)