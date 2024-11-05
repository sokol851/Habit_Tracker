from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from habit_tracker.models import Habit
from habit_tracker.paginators import CustomPagination
from habit_tracker.serailizers import HabitSerializer
from users.premissions import IsOwner


@extend_schema_view(
    list=extend_schema(summary="Отображение списка своих привычек", ),
    update=extend_schema(summary="Изменение своей привычки", ),
    retrieve=extend_schema(summary="Детализация своей привычки", ),
    partial_update=extend_schema(summary='Изменение части своей привычки'),
    create=extend_schema(summary="Создание своей привычки", ),
    destroy=extend_schema(summary="Удаление своей привычки", ),
)
class HabitViewSet(viewsets.ModelViewSet):
    """ ViewSet для работы со своими привычками """

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


@extend_schema(summary='Отображение списка публичных привычек')
class HabitPublicListAPIView(generics.ListAPIView):
    """ Отображение списка публичных привычек """

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
