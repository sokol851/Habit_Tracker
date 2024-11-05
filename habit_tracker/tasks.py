import pytz
from celery import shared_task

from config import settings
from habit_tracker.models import Habit

import datetime
from habit_tracker.services import send_telegram_message


@shared_task
def send_habit():
    """ Отправка задачи в планировщик """

    zone = pytz.timezone(settings.TIME_ZONE)
    current_time = datetime.datetime.now(zone)
    current_time_less = current_time - datetime.timedelta(minutes=1)
    habits = Habit.objects.filter(time__lte=current_time.time(), time__gte=current_time_less.time())
    for habit in habits:
        id_user_telegram = habit.user.id_user_telegram
        message = f"Настало время для {habit.action} в {habit.time} в {habit.place}"
        send_telegram_message(id_user_telegram, message)
