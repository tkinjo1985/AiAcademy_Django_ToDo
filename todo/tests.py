from django.test import TestCase, Client
from accounts.models import CustomUser
from todo.models import ToDo

from bs4 import BeautifulSoup


class ToDoViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = CustomUser.objects.create_user(
            username='test_user',
            email=None,
            password='hrcwn098'
        )

    def test_add_todo(self):
        self.client.force_login(self.test_user)
        ToDo.objects.create(user_id=self.test_user.id,
                            name='todo_add_test', content='todo_add_test')
        response = self.client.get('/')
        soup = BeautifulSoup(response.content, features="lxml")
        todo_id = soup.find(id='todo_id').text

        self.assertEqual(todo_id, str(ToDo.objects.filter(
            user_id=self.test_user.id).first().id))
