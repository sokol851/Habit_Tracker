import requests
from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL


def send_telegram_message(chat_id, message):
    """ Отправка сообщения в телеграм чат """

    params = {
        'text': message,
        'chat_id': chat_id,
    }

    try:
        requests.get(
            f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage",
            params=params, timeout=5)
    except requests.exceptions.Timeout:
        print("Истекло время ожидания ответа сервера Телеграм.")
