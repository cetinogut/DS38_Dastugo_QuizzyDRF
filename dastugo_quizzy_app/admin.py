from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = [
        'name',
        ]

@admin.register(models.Quizzy)
class QuizAdmin(admin.ModelAdmin):
	list_display = [
        'id', 
        'title',
        ]

class AnswerInlineModel(admin.TabularInline): # have to define the inline and use later below
    model = models.Answer
    fields = [
        'answer_text', 
        'is_right'
        ]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'quiz',
        'question_text',
        ]
    list_display = [
        'question_text', 
        'quiz',
        'date_updated'
        ]
    inlines = [
        AnswerInlineModel, 
        ] 

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text', 
        'is_right', 
        'question'
        ]