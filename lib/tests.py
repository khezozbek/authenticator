from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Password
from .serializers import PasswordSerializers


class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.password = Password.objects.create(user=self.user, address='Test Address', password='Test Password')

    def test_create_password_view(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        response = self.client.get(reverse('detail', args=[self.password.pk]))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)


class SerializerTestCase(TestCase):
    def setUp(self):
        self.password_data = {
            'address': 'Test Address',
            'password': 'Test Password'
        }
        self.serializer = PasswordSerializers(data=self.password_data)

    def test_valid_serializer(self):
        self.assertTrue(self.serializer.is_valid())

    def test_invalid_serializer(self):
        self.password_data['address'] = ''
        self.assertFalse(self.serializer.is_valid())

    def test_serializer_save(self):
        self.assertTrue(self.serializer.is_valid())
        password_instance = self.serializer.save()
        self.assertIsInstance(password_instance, Password)
