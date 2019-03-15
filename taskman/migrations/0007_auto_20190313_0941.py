# Generated by Django 2.1.7 on 2019-03-13 09:41

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskman', '0006_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='task',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taskman.Team'),
        ),
        migrations.RemoveField(
            model_name='task',
            name='assignee',
        ),
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.ManyToManyField(default=django.contrib.auth.models.User, related_name='assignee', to=settings.AUTH_USER_MODEL),
        ),
    ]