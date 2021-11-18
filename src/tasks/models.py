from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    # Модель задачи
    name = models.CharField(max_length=255, verbose_name='Название задачи')
    description = models.TextField(blank=True, verbose_name='Описание задачи')
    end_date = models.DateField(verbose_name='Дата завершения')
    file = models.FileField(blank=True, null=True, verbose_name='Прикрепленный документ')
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks_created', verbose_name='Создатель'
    )
    performers = models.ManyToManyField(
        User, related_name='tasks_performed', verbose_name='Исполнители'
    )

    def __str__(self):
        return f"Task: {self.name}"
