## Сервис для отслеживания привычек
### В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.

#### Запуск сервера через docker-compose:
    1) Установить docker следуя инструкции на сайте для своей ОС: https://www.docker.com/
    2) .env.example переименовать в .env
    3) Заполнить .env
    4) Запустить командой: "docker-compose up -d --build"
    5) Если .env заполнен верно - создадутся 5 объединённых контейнеров.
    6) Сервер доступен по адресу: http://0.0.0.0:8000/

#### Для создания администратора введите команду:
    Из терминала: docker exec -it habit_tracker_app_1 sh -c "python manage.py csu"
    Из docker-desktop: python manage.py csu

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
