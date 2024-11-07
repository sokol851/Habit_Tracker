from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserDestroyAPIView,
                         UserListAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView, MyTokenObtainPairView,
                         MyTokenRefreshView)

app_name = UsersConfig.name

urlpatterns = [
    path("users/", UserListAPIView.as_view(),
         name="user-list"),
    path("users/create/", UserCreateAPIView.as_view(),
         name="user-create"),
    path("users/<int:pk>/update/", UserUpdateAPIView.as_view(),
         name="user-update"),
    path("users/<int:pk>/", UserRetrieveAPIView.as_view(),
         name="user-retrieve"),
    path("users/<int:pk>/destroy/", UserDestroyAPIView.as_view(),
         name="user-destroy"),

    path("token/", MyTokenObtainPairView.as_view(
        permission_classes=[AllowAny]), name="token_obtain_pair"),
    path("token/refresh/", MyTokenRefreshView.as_view(
        permission_classes=[AllowAny]), name="token_refresh"),
]
