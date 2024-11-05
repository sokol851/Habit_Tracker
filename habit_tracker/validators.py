from datetime import timedelta

from rest_framework.serializers import ValidationError


class RewardValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        tmp_val1 = dict(value).get(self.field1)
        tmp_val2 = dict(value).get(self.field2)
        if tmp_val1 and tmp_val2:
            raise ValidationError(
                "Вы не можете заполнить 'Вознаграждение' и 'Приятную привычку' одновременно!"
            )


class PleasantActionValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = value.get(self.field)
        if tmp_val:
            if not tmp_val.pleasant_sign:
                raise ValidationError(
                    "Связанная привычка может быть только приятной!"
                )


class TimeHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = value.get(self.field)
        if tmp_val and tmp_val > timedelta(seconds=120):
            raise ValidationError("Время на выполнение привычки не должно превышать 2 минут!")


class PleasantHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val:
            values = dict(value)
            if (
                    values.get("reward") is not None
                    or values.get("pleasant_action") is not None
            ):
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения или связанной привычки!"
                )


class RegularityValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val is not None:
            if int(tmp_val) < 1:
                raise ValidationError("Нельзя выполнять привычку реже 1 раза в неделю.")
            if int(tmp_val) > 7:
                raise ValidationError("Нельзя выполнять привычку чаще 7 раз в неделю.")
