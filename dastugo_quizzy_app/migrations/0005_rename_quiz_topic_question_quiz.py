# Generated by Django 3.2.9 on 2021-11-28 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dastugo_quizzy_app', '0004_auto_20211129_0002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quiz_topic',
            new_name='quiz',
        ),
    ]
