# Generated by Django 3.2.9 on 2021-11-20 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='flight',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='passenger',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.DeleteModel(
            name='Flight',
        ),
        migrations.DeleteModel(
            name='Passanger',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
