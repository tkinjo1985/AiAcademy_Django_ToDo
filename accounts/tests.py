from django.test import TestCase, Client
from accounts.models import CustomUser


class UserAuthenticatTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = CustomUser.objects.create_user(
            username='test_user',
            password='hrcwn098'
        )

    def test_user_not_login(self):
        response = self.client.get('/')

        # status_codeが302(リダイレクト)であること
        self.assertEqual(response.status_code, 302)
        # ログインページへリダイレクトされる
        self.assertEqual(response.url, '/accounts/login/?next=/')

    def test_user_login(self):
        self.client.force_login(self.test_user)
        response = self.client.get('/')

        # status_codeが200である
        self.assertEqual(response.status_code, 200)
        # contextにin_progress_todoが含まれている
        self.assertTrue('in_progress_todo' in response.context)
        # template_nameがtodo/index.htmlであること
        self.assertEqual(response.template_name, ['todo/index.html'])
