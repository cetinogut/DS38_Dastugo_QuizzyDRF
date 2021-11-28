from rest_framework import serializers
from .models import Quizzy, Question, Answer


class QuizzySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizzy
        fields = [
            'title',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'title','answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizzySerializer(read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'quiz','question_text','answer',
        ]