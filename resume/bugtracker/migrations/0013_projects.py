# Generated by Django 3.0.4 on 2020-06-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0012_auto_20200616_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=140)),
            ],
        ),
    ]