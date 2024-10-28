from django.urls import path
from rest_framework.routers import DefaultRouter

from habit_tracker.apps import HabitTrackerConfig
from habit_tracker.views import HabitViewSet, HabitPublicListAPIView

app_name = HabitTrackerConfig.name

router = DefaultRouter()
router.register(r"habit", HabitViewSet, basename="habit")

urlpatterns = [
                  path('public/', HabitPublicListAPIView.as_view(), name='public_list')
              ] + router.urls
