from rest_framework import serializers

from rest_framework import fields
from habit_tracker.models import Habit, PERIODICAL
from habit_tracker.validators import RewardValidator, PleasantActionValidator, TimeHabitValidator, \
    PleasantHabitValidator, RegularityValidator


class CustomMultipleChoiceField(fields.MultipleChoiceField):
    def to_representation(self, value):
        return list(super().to_representation(value))


class HabitSerializer(serializers.ModelSerializer):
    periodical = CustomMultipleChoiceField(choices=PERIODICAL, required=False)

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
