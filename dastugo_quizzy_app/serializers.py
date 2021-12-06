from rest_framework import serializers
from .models import Quizzy, Question, Answer, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "quiz_count"
        )


class CategoryQuizzesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzy
        fields = (
            "title",
            "question_count",
        )

class QuizzySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzy
        fields = [
            'title',
            'question_count',
            
        ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer): #bring one question based on quiz title
    #answer = serializers.StringRelatedField(many=True) #only answer_text is returned here, no correct answer or other fields.
    answer = AnswerSerializer(many=True, read_only=True) # realtion exists so we ca nreturn all fields to the front end
    class Meta:
        model = Question
        fields = [
            'question_text','answer', 'explanation_of_answer', # get the answers to this question based on the foreign key
        ]


class QuestionSerializer(serializers.ModelSerializer): # bring all questions based on quiz title (topic)
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizzySerializer(read_only=True) # get the quiz topic
    class Meta:
        model = Question
        fields = [
            'quiz','question_text','answer','explanation_of_answer',
        ]