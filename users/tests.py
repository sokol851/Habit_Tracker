from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from users.models import User


class UserTest(APITestCase):
    """ Тест пользователя """

    def test_user(self):
        url = reverse("users:user-create")
        user = {"id": 1, "email": "test@testtest.ru", "password": "12345"}
        response = self.client.post(url, data=user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        get_user = User.objects.get(id=1)
        self.assertEqual(get_user.__str__(), "test@testtest.ru")
        data = response.json()
        self.assertEqual(data['email'], "test@testtest.ru")

        self.client.force_authenticate(user=get_user)
        url = reverse("users:user-update", args=(get_user.pk,))
        user = {"password": "123"}
        response = self.client.patch(url, data=user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
