from celery import shared_task
from habit_tracker.models import Habit

import datetime
from habit_tracker.services import send_telegram_message


@shared_task
def send_habit():
    habits = Habit.objects.all()
    current_date = datetime.datetime.now()  # Текущее время
    for habit in habits:
        if habit.time >= current_date.time():
            id_user_telegram = habit.user.id_user_telegram
            message = f"Я буду {habit.action} в {habit.time} в {habit.place}."
            send_telegram_message(id_user_telegram, message)  # Отправляем привычку в Telegram чат
