# from django.utils import timezone
from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from habit_tracker.models import Habit
from habit_tracker.paginators import CustomPagination
from habit_tracker.serailizers import HabitSerializer
# from habit_tracker.services import send_telegram_message
from users.premissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user.pk).order_by("id")

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination

    # now = timezone.now()
    # print(f"Время: {now}")
    # habits = Habit.objects.filter(
    #     time__lte=now,
    #     time__gt=now - timezone.timedelta(minutes=1)
    # )
    # print(f"Найдено привычек: {habits.count()}")
    # print(habits)
    # for habit_item in habits:
    #     print(habit_item.time)
    #     if habit_item.user.id_user_telegram:
    #         # send_telegram_message(habit_item.user.id_user_telegram , habit_item)
    #         habit_item.time = habit_item.time + timezone.timedelta(days=habit_item.periodical)
    #         habit_item.save()
    #         print(habit_item.time)
    #     else:
    #         print(f"У пользователя {habit_item.user} не указан тг")
