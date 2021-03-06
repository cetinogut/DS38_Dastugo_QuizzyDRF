# Generated by Django 3.2.9 on 2021-11-28 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dastugo_quizzy_app', '0005_rename_quiz_topic_question_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(choices=[(0, 'Rookie'), (1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Artist')], default=0, verbose_name='Difficulty'),
        ),
    ]
