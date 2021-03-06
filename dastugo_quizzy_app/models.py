from django.db import models
from django.utils.translation import gettext_lazy as _ # potential items for translation gets _ in front


class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = _("Kategori") 
        verbose_name_plural = _("Categories") # plural names can be identified for irregularities
        ordering = ['name']
        
    def __str__(self):
        return self.name

    @property
    def quiz_count(self):
        return self.quizzy_set.count()
    
class Quizzy(models.Model):
    title = models.CharField(max_length=255, default=_(
        "New Quiz"), verbose_name=_("Quiz Topic")) # verbose name is the table title in admin panel, but I chnaged it to Quiz Topic which is more understandable 
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING) # use case 21: I don't want the category to be deleted when I delete a category
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Sınav") # table name what we want to put
        verbose_name_plural = _("Quizzies") # plural names can be identified for irregularities
        ordering = ['id']
        
    @property
    def question_count(self):
        #return self.question_set.count() # I used related_name in Question model as question. for this reason question_set is not defined and does not work correctly. The solution is the line below.
        return self.question.count()

class Updated(models.Model): # this is an abstract class that we wil luse to pass the updated datetime filed for question and answer. Dont repeat yourself

    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True

class Question(Updated): # instead of models.Model we have our own abstract class to inherit.

    SCALE = ( # numbers might give better performance during the query..
        (0, _('Rookie')), # ready to translate
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Artist'))
    )

    TYPE = (
        (0, _('Multiple Choice')),
        (1, _('True-False Choice')), # TODO
    )

    quiz = models.ForeignKey(
        Quizzy, related_name='question', on_delete=models.DO_NOTHING) 
    technique = models.IntegerField(
        choices=TYPE, default=0, verbose_name=_("Type of Question"))
    question_text = models.CharField(max_length=255, verbose_name=_("Question"))
    explanation_of_answer = models.CharField(max_length=255, verbose_name=_("Explanation"), null=True, blank=True)
    difficulty = models.IntegerField(
        choices=SCALE, default=0, verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.question_text
    
    class Meta:
        verbose_name = _("Soru")
        verbose_name_plural = _("Questions")
        ordering = ['id']
    

""" The related_name attribute specifies the name of the reverse relation from the Quizzy model back to your model.
If you don't specify a related_name, Django automatically creates one using the name of your model with the suffix _set, for instance Quizzy.question_set.all().
If you do specify, e.g. related_name=question on the Quizzy model, Quizzy.question_set will still work, but the Quizzy.question. syntax is obviously a bit cleaner and less clunky; so for example, if you had a user object current_user, you could use current_user.maps.all() to get all instances of your Map model that have a relation to current_user.
 """
class Answer(Updated):

    class Meta:
        verbose_name = _("Seçenek")
        verbose_name_plural = _("Seçenekler")
        ordering = ['id']

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField( 
        max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False, verbose_name=_("Doğru Seçenek mi?"))

    def __str__(self):
        return self.answer_text