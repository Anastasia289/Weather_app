# Weather_app
Приложение для получения информации о погоде. Пользователь вводит название города,  и получает для него прогноз погоды на ближайшее время.


После применения миграций база автоматически заполнится тестовыми данными
В админку можно зайти используя пару:
email:'admin@admin.ru',
password: 'admin'


подключен swagger
сделана возможность регистрации и авторизации на сайте


вставьте свой api ключ


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