from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserTasksListView

router = DefaultRouter()
router.register(r'', TaskViewSet, basename='tasks')

urlpatterns = [
    path('my/', UserTasksListView.as_view(), name='my-tasks'),
    path('', include(router.urls)),
]