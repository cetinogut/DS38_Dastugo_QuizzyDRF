from django.contrib import admin
from . import models

class QuizzyInlineModel(admin.TabularInline): # have to define the inline and use later below
    model = models.Quizzy
    extra = 0 
    fields = [
        'title', 
        'question_count',
        ]
    readonly_fields = ('question_count',)
    
#@admin.register(models.Category)
admin.site.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'quizzy_count',
        ]
    fields = ['name', ('quizzy_count')] # quiz_count is a added property. To show this one in admin panel also add the line below for read only field
    readonly_fields = ('quizzy_count',)
    inlines = [
        QuizzyInlineModel,
        ]   
    
@admin.register(models.Quizzy)
class QuizAdmin(admin.ModelAdmin):
	list_display = [
        'id', 
        'title',
        'category',
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
        'date_updated',
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