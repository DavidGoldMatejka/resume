# Generated by Django 3.0.4 on 2020-06-19 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugtracker', '0016_auto_20200617_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprojects',
            name='project_manager',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]