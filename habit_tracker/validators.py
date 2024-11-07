from datetime import timedelta

from rest_framework.serializers import ValidationError


class RewardValidator:
    """ Проверка на установку двух полей поощрения одновременно """

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        tmp_val1 = value.get(self.field1)
        tmp_val2 = value.get(self.field2)
        if tmp_val1 and tmp_val2:
            raise ValidationError(
                "Вы не можете заполнить 'Вознаграждение'"
                " и 'Приятную привычку' одновременно!"
            )


class PleasantActionValidator:
    """ Проверка связанной привычки на приятность """

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
    """ Проверка времени на выполнение привычки """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = value.get(self.field)
        if tmp_val and tmp_val > timedelta(seconds=120):
            raise ValidationError("Время на выполнение привычки "
                                  "не должно превышать 2 минут!")


class PleasantHabitValidator:
    """ Проверка отсутствия поощрения у приятной привычки """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = value.get(self.field)
        if tmp_val:
            if (value.get("reward") is not None
                    or value.get("pleasant_action") is not None):
                raise ValidationError(
                    "У приятной привычки не может быть"
                    " вознаграждения или связанной привычки!"
                )


class RegularityValidator:
    """ Проверка времени выполнения привычки """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = value.get(self.field)
        if tmp_val is not None:
            if int(tmp_val) < 1:
                raise ValidationError("Нельзя выполнять привычку "
                                      "реже 1 раза в неделю.")
            if int(tmp_val) > 7:
                raise ValidationError("Нельзя выполнять привычку "
                                      "чаще 7 раз в неделю.")
