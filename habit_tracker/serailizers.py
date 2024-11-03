from rest_framework import serializers

from rest_framework import fields
from habit_tracker.models import Habit
from habit_tracker.validators import RewardValidator, PleasantActionValidator, TimeHabitValidator, \
    PleasantHabitValidator, RegularityValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardValidator(field1="reward", field2="pleasant_action"),
            PleasantActionValidator(field="pleasant_action"),
            TimeHabitValidator(field="time_habit"),
            PleasantHabitValidator(field="pleasant_sign"),
            RegularityValidator(field="periodical"),
        ]
