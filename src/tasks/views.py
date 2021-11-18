from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .permissions import IsCreator
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    # CRUD задачи
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()

    def get_permissions(self):
        if self.request.method in ('PUT', 'DELETE'):
            self.permission_classes = (IsCreator,)
        else:
            self.permission_classes = (IsAuthenticated,)

        return super().get_permissions()

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)


class UserTasksListView(generics.ListAPIView):
    # Список задач, созданных текущим пользователем
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user)
