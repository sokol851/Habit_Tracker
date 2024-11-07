from datetime import time, timedelta

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from habit_tracker.models import Habit
from users.models import User


class HabitTest(APITestCase):
    """ Тест CRUD привычек """

    def setUp(self):
        self.user = User.objects.create(id=50,
                                        email="test@test.ru",
                                        password="12345")
        self.pleasant_action = Habit.objects.create(
            id=100,
            action="TestPleasant",
            time=time(0, 0, 0),
            pleasant_sign=True,
            periodical=1,
            time_habit=timedelta(0, 0, 0, 0, 2),
            user=self.user)
        self.action = Habit.objects.create(
            id=200,
            action="TestHabit",
            time=time(0, 30, 0),
            periodical=1,
            time_habit=timedelta(0, 0, 0, 0, 2),
            pleasant_action=self.pleasant_action,
            user=self.user,
            is_public=True)
        self.client.force_authenticate(user=self.user)

    def test_list_habit(self):
        response = self.client.get('/habit/')
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data.get("results")), Habit.objects.count())
        self.assertEqual(data.get("results"), [
            {'id': 100,
             'place': 'Везде',
             'time': '00:00:00',
             'action': 'TestPleasant',
             'pleasant_sign': True,
             'periodical': 1,
             'reward': None,
             'time_habit': '00:02:00',
             'is_public': False,
             'user': 50,
             'pleasant_action': None
             },
            {'id': 200,
             'place': 'Везде',
             'time': '00:30:00',
             'action': 'TestHabit',
             'pleasant_sign': False,
             'periodical': 1,
             'reward': None,
             'time_habit': '00:02:00',
             'is_public': True,
             'user': 50,
             'pleasant_action': 100
             }])

    def test_list_habit_is_public(self):
        url = reverse("habit_tracker:public_list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data.get("results")),
                         Habit.objects.filter(is_public=True).count())
        self.assertEqual(data.get("results"),
                         [
                             {'id': 200,
                              'place': 'Везде',
                              'time': '00:30:00',
                              'action': 'TestHabit',
                              'pleasant_sign': False,
                              'periodical': 1,
                              'reward': None,
                              'time_habit': '00:02:00',
                              'is_public': True,
                              'user': 50,
                              'pleasant_action': 100
                              }
                         ]
                         )

    def test_patch_habit(self):
        data = {'action': 'Test_Renamed'}
        response = self.client.patch(f'/habit/{self.action.pk}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data,
                         {'id': 200,
                          'place': 'Везде',
                          'time': '00:30:00',
                          'action': 'Test_Renamed',
                          'pleasant_sign': False,
                          'periodical': 1,
                          'reward': None,
                          'time_habit': '00:02:00',
                          'is_public': True,
                          'user': 50,
                          'pleasant_action': 100
                          }
                         )

    def test_create_habit(self):
        data = {
            "action": "TestHabitNew",
            "time": time(15, 30, 0),
            "periodical": 1,
            "time_habit": timedelta(0, 0, 0, 0, 2)
        }
        response = self.client.post(r'/habit/', data=data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data, {
            'id': 201,
            'place': 'Везде',
            'time': '15:30:00',
            'action': 'TestHabitNew',
            'pleasant_sign': False,
            'periodical': 1,
            'reward': None,
            'time_habit': '00:02:00',
            'is_public': False,
            'user': 50,
            'pleasant_action': None
        })
        get_habit = Habit.objects.get(id=201)
        self.assertEqual(get_habit.__str__(), "TestHabitNew")

    def test_create_wrong_habits(self):
        data = {
            'id': 201,
            'place': 'Везде',
            'time': '15:30:00',
            'action': 'Wrong_time_habit',
            'periodical': 1,
            'time_habit': '00:03:00',
            'is_public': False,
            'user': 50,
        }
        response = self.client.post(r'/habit/', data=data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            data['non_field_errors'][0],
            'Время на выполнение привычки не должно превышать 2 минут!')

        data2 = {
            'id': 201,
            'place': 'Везде',
            'time': '15:30:00',
            'action': 'Wrong_periodical',
            'periodical': 0,
            'time_habit': '00:02:00',
            'is_public': False,
            'user': 50,
        }
        response = self.client.post(r'/habit/', data=data2)
        data2 = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            data2['non_field_errors'][0],
            'Нельзя выполнять привычку реже 1 раза в неделю.')

        data3 = {
            'id': 201,
            'place': 'Везде',
            'time': '15:30:00',
            'action': 'Wrong_periodical_2',
            'periodical': 8,
            'time_habit': '00:02:00',
            'is_public': False,
            'user': 50,
        }
        response = self.client.post(r'/habit/', data=data3)
        data3 = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            data3['non_field_errors'][0],
            'Нельзя выполнять привычку чаще 7 раз в неделю.')

        data4 = {
            'id': 201,
            'place': 'Везде',
            'time': '15:30:00',
            'action': 'Wrong_for_pleasant',
            'periodical': 8,
            'time_habit': '00:02:00',
            'is_public': False,
            'user': 50,
            'pleasant_sign': True,
            'reward': 'вознаграждение'
        }
        response = self.client.post(r'/habit/', data=data4)
        data4 = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            data4['non_field_errors'][0],
            'У приятной привычки не может быть вознаграждения'
            ' или связанной привычки!')

        data5 = {
            'id': 201,
            'place': 'Везде',
            'time': '15:30:00',
            'action': 'Wrong_pleasant_action',
            'periodical': 8,
            'time_habit': '00:02:00',
            'is_public': False,
            'user': 50,
            'pleasant_action': 200
        }
        response = self.client.post(r'/habit/', data=data5)
        data5 = response.json()
        # print(data3['non_field_errors'][0])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            data5['non_field_errors'][0],
            'Связанная привычка может быть только приятной!')

        data5 = {
            'id': 201,
            'place': 'Везде',
            'time': '15:30:00',
            'action': 'Wrong_reward_and_pleasant_action',
            'periodical': 8,
            'time_habit': '00:02:00',
            'is_public': False,
            'user': 50,
            'pleasant_action': 100,
            'reward': 'вознаграждение'
        }
        response = self.client.post(r'/habit/', data=data5)
        data5 = response.json()
        # print(data3['non_field_errors'][0])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            data5['non_field_errors'][0],
            "Вы не можете заполнить 'Вознаграждение'"
            " и 'Приятную привычку' одновременно!")

    def test_delete_habit(self):
        response = self.client.delete(f'/habit/{self.action.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
