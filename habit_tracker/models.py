from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    PERIODICAL = (
        ('1', 'Понедельник'),
        ('2', 'Вторник'),
        ('3', 'Среда'),
        ('4', 'Четверг'),
        ('5', 'Пятница'),
        ('6', 'Суббота'),
        ('7', 'Воскресенье'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', **NULLABLE,
                             on_delete=models.CASCADE)
    place = models.CharField(max_length=100, verbose_name='Место', default='Везде')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=150, verbose_name='Привычка')
    pleasant_sign = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    pleasant_action = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Приятная привычка',
                                        **NULLABLE)
    periodical = MultiSelectField(max_length=7, max_choices=7, choices=PERIODICAL, verbose_name='Периодичность')
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение', **NULLABLE)
    time_habit = models.TimeField(verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ['-id']

    def __str__(self):
        return self.action
