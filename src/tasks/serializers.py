from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # Сериализатор пользователя
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        read_only_fields = ('username', 'first_name', 'last_name', 'email',)


class TaskSerializer(serializers.ModelSerializer):
    # Сериализатор задачи
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('name', 'description', 'end_date', 'file', 'creator', 'performers',)
        read_only_fields = ('creator',)

