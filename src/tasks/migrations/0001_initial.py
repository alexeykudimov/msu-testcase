# Generated by Django 3.2.9 on 2021-11-18 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('description', models.TextField(blank=True, verbose_name='Описание задачи')),
                ('end_date', models.DateField(verbose_name='Дата завершения')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Прикрепленный документ')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_created', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('performers', models.ManyToManyField(related_name='tasks_performed', to=settings.AUTH_USER_MODEL, verbose_name='Исполнители')),
            ],
        ),
    ]