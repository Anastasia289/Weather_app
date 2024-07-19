# Weather_app
Приложение для получения информации о погоде. Пользователь вводит название города,  и получает для него прогноз погоды на ближайшее время.

получить токен
http://127.0.0.1:8000/v1/jwt/create/
{
  "email": "admin@admin.ru",
  "password": "admin"
}

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMTQ4MTU0OCwiaWF0IjoxNzIxMzk1MTQ4LCJqdGkiOiIwZjZlOGE4MjZkZDA0YTNhYmFiYWMwODdhNDYwNzg0ZiIsInVzZXJfaWQiOjF9.L8crhepEGct-w0pZb84v13jJ0bZoTr_lxxtfU5T7omc",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxNDgxNTQ4LCJpYXQiOjE3MjEzOTUxNDgsImp0aSI6IjRiM2UxYjgyM2Y4YzRlMjJhM2ZlYjE1MzJjNDhiM2ZhIiwidXNlcl9pZCI6MX0.ispdcbyjDLDizXV2DpvidLlyZa5Z6eAbqzrTFXUyylw"
}

После применения миграций база автоматически заполнится тестовыми данными
В админку можно зайти используя пару:
{
  "email": "admin@admin.ru",
  "password": "admin"
}


подключен swagger
сделана возможность регистрации и авторизации на сайте


вставьте свой api ключ (указан тестовый. для удобства работы поставьте свой)


Как получить API ключ OpenWeatherMap
Чтобы получить API ключ OpenWeatherMap, следуйте этим простым шагам:

Зарегистрируйтесь на сайте OpenWeatherMap: Перейдите на официальный сайт OpenWeatherMap.
Заполните форму регистрации: Введите свой адрес электронной почты, создайте пароль и подтвердите его. Заполните необходимые поля и нажмите кнопку "Sign Up" (Зарегистрироваться).
Подтвердите свой аккаунт: После завершения регистрации вам придет письмо на указанный адрес электронной почты с инструкциями по подтверждению аккаунта. Перейдите по ссылке в письме для подтверждения.
Войдите в свой аккаунт: После подтверждения аккаунта вернитесь на сайт OpenWeatherMap и войдите в свой аккаунт, используя адрес электронной почты и пароль, которые вы указали при регистрации.
Получите API ключ: После входа в аккаунт перейдите на страницу My API Keys. Здесь вы найдете свой уникальный API ключ, который можно использовать для доступа к погодным данным через API OpenWeatherMap.
Сохраните ключ: Скопируйте свой API ключ. Обязательно храните свой ключ в безопасном месте, так как он будет использоваться в ваших приложениях или скриптах для доступа к погодным данным.


сделана загрузка городов
# python manage.py load_cities
# docker-compose exec backend python manage.py load_cities