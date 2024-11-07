## Сервис для отслеживания привычек
### В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.

#### Запуск сервера:
    1) Заменить .env.example на .env
    2) Заполнить .env
    3) Применить миграции в базу
    4) Запустить командой: python manage.py runserver

#### Для создания администратора введите команду:
    "python manage.py csu"

#### Запуск планировщика задач:
    celery -A config worker -l INFO
    celery -A config beat -l INFO -S django

#### Поля привычек:
    user - Создатель привычки
    place - Место для совершения привычки
    time - Время совершения привычки
    action - Действие привычки
    pleasant_sign - Признак полезной привычки
    pleasant_action - Связаная полезная привычка
    periodical - Периодичность выполнения привычки в днях (не менее 1 дня в неделю)
    reward - Вознаграждение
    time_habit - Время на совершение привычки (не более 2 минут)
    is_public - Признак публичности

#### Поля пользователя:
    email - Почта
    password - Пароль
    first_name - Имя
    last_name - Фамилия
    phone - Телефон
    id_user_telegram - ID пользователя Telegram
    avatar - Аватар
