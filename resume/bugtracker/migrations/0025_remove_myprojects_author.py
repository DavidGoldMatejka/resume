# Generated by Django 3.0.4 on 2020-06-20 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0024_myprojects_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprojects',
            name='author',
        ),
    ]