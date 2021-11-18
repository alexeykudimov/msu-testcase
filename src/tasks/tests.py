from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TasksTest(APITestCase):

    def setUp(self):
        self.test_user1 = User.objects.create_user(username='test_user1', password='202020')
        self.test_user1.save()
        self.test_user2 = User.objects.create_user(username='test_user2', password='303030')
        self.test_user2.save()

        self.task_json = {
            "name": "Test task",
            "description": "Description test task",
            "end_date": "2021-12-31",
            "file": None,
            "performers": [self.test_user2]
        }

        self.updated_task_json = {
            "name": "Updated Test task",
            "description": "Updated Description test task",
            "end_date": "2022-12-31",
            "file": None,
            "performers": [self.test_user2]
        }

    def test_auth_user1(self):
        # Получаем токен первого пользователя
        resp = self.client.post(
            reverse('token_obtain_pair'),
            {'username': 'test_user1', 'password': '202020'},
            format='json'
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        self.token_user1 = resp.data['access']

    def test_auth_user2(self):
        # Получаем токен второго пользователя
        resp = self.client.post(
            reverse('token_obtain_pair'),
            {'username': 'test_user1', 'password': '202020'},
            format='json'
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        self.token_user2 = resp.data['access']

    def test_create_task(self):
        # Создаем задачу первым пользователем
        self.client.credentials(HTTP_AUTORIZATION=f'JWT {self.token_user1}')
        resp = self.client.post(reverse('tasks-create'), self.task_json, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_list_task(self):
        # Проверяем список задач
        self.client.credentials(HTTP_AUTORIZATION=f'JWT {self.token_user1}')
        resp = self.client.get(reverse('tasks-list'))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_fail_update_task(self):
        # Пытаемся обновить чужую задачу
        self.client.credentials(HTTP_AUTORIZATION=f'JWT {self.token_user2}')
        resp = self.client.put(reverse('tasks-update', 1), self.updated_task_json, format='json')
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_task(self):
        # Обновляем свою задачу
        self.client.credentials(HTTP_AUTORIZATION=f'JWT {self.token_user1}')
        resp = self.client.put(reverse('tasks-update', 1), self.updated_task_json, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_fail_destroy_task(self):
        # Пытаемся удалить чужую задачу
        self.client.credentials(HTTP_AUTORIZATION=f'JWT {self.token_user2}')
        resp = self.client.delete(reverse('tasks-destroy', 1))
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_destroy_task(self):
        # Удаляем свою задачу
        self.client.credentials(HTTP_AUTORIZATION=f'JWT {self.token_user1}')
        resp = self.client.delete(reverse('tasks-destroy', 1))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_user1_tasks(self):
        # Список задач, созданных первым пользователем (одна)
        self.client.credentials(HTTP_AUTORIZATION=f'JWT {self.token_user1}')
        resp = self.client.delete(reverse('my-tasks'))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(len(resp.data) == 1)

    def test_user2_tasks(self):
        # Список задач, созданных вторым пользователем (ноль)
        self.client.credentials(HTTP_AUTORIZATION=f'JWT {self.token_user2}')
        resp = self.client.delete(reverse('my-tasks'))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(len(resp.data) == 0)

