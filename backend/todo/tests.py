
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def create_task(self):
        return self.client.post('/api/tasks/', {
            'title': 'Test Task',
            'description': 'This is a test task',
            'status': 'pending',
            'due_date': '2023-12-31'
        }, format='json')

    def test_create_task(self):
        response = self.create_task()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_update_task(self):
        response = self.create_task()
        task_id = response.data['id']
        url = f'/api/tasks/{task_id}/'
        updated_data = {
            'title': 'Updated Test Task',
            'status': 'completed',
            'due_date': '2023-12-25'
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=task_id).title, 'Updated Test Task')

    def test_delete_task(self):
        response = self.create_task()
        task_id = response.data['id']
        url = f'/api/tasks/{task_id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
