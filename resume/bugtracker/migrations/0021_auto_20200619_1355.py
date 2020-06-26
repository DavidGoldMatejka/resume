# Generated by Django 3.0.4 on 2020-06-19 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugtracker', '0020_post_assigned_developer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='assigned_developer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]