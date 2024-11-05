from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.models import User
from users.serializers import UserSerializer


@extend_schema(summary='Список пользователей')
class UserListAPIView(generics.ListAPIView):
    """ Список пользователей """

    serializer_class = UserSerializer
    queryset = User.objects.all()


@extend_schema(summary='Создание пользователя')
class UserCreateAPIView(generics.CreateAPIView):
    """ Создание пользователя """

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


@extend_schema(summary='Редактирование пользователя')
class UserUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_update(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


@extend_schema(summary='Удаление пользователя')
class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление пользователя """

    queryset = User.objects.all()


@extend_schema(summary='Детализация пользователя')
class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Детализация пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()


@extend_schema(summary='Авторизация пользователя')
class MyTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(summary='Обновление токена')
class MyTokenRefreshView(TokenRefreshView):
    pass
