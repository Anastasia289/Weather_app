from django.shortcuts import render

# # Запрос текущей погоды по коду города
# # https://api.openweathermap.org/data/2.5/weather?id=498817&units=metric&appid=2f3c1bad2f3c1bad2f3c1bad2f3c1bad&lang=ru
# # Параметры запроса:
# # id – обязательный параметр. Идентификатор города. Список городов с идентификатором «city.list.json.gz» можно скачать здесь .
# # appid – обязательный параметр. Ваш уникальный API-ключ.
# # mode – необязательный параметр. Формат ответа. Возможные значения: xml и html. Если параметр не указан, то по умолчанию используется json.
# # units – необязательный параметр. Единицы измерения. Доступные варианты: standard, metricи imperial. По умолчанию используется standard.
# # lang – необязательный параметр. Язык ответа.
# # https://api.openweathermap.org/data/2.5/weather?id={{'id города'}}&units=metric&appid={{ключ из апи}}&lang=ru

# https://api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key} - это верно
# # Коды ошибок в ответах на запросы
# # 401 – эта ошибка связанна с API-ключом. Возможные причины:

# # API-ключ не указан.
# # API-ключ не активирован. В данном случае необходимо повторить запрос через несколько часов.
# # Неправильно указан API-ключ.
# # Используется API-ключ бесплатного тарифа для получения данных из платного тарифа.
# # 404 – эта ошибка связана с неправильным запросом. Возможные причины:

# # Указано неправильное название города, почтовый индекс или идентификатор города.
# # Неправильный запрос к API. Проверьте запрос на ошибки. Используйте примеры запросов из документации.
# # 429 – эта ошибка связана с API-ключом. Ошибка возникает при превышении лимитов тарифа.

from django.shortcuts import render
import requests
import json

def index(request):
    data = {}  # Initialize data as empty for both GET and POST requests

    if request.method == "POST":
        city = request.POST.get('city')
        if city:
            try:
                response = requests.get(
                    url=f'https://api.openweathermap.org/data/2.5/weather?id={city}&appid=73d4eb76b4a0c408fd16f3acc5cb28f4'
                    # url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=73d4eb76b4a0c408fd16f3acc5cb28f4'
                )
                response.raise_for_status()  # Raise an error for bad status codes
                list_of_data = response.json()

                data = {
                    "city": city,  # Add the city name to the data dictionary
                    "country_code": str(list_of_data['sys']['country']),
                    'coordinate': f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
                    'temp': f"{list_of_data['main']['temp']} (min: {list_of_data['main']['temp_min']})",
                    'pressure': str(list_of_data['main']['pressure']),
                    'humidity': str(list_of_data['main']['humidity']),
                }
                print(data)

            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except requests.exceptions.RequestException as req_err:
                print(f"Error occurred: {req_err}")
            except json.JSONDecodeError as json_err:
                print(f"JSON decode error: {json_err}")

    return render(request, "index.html", {'data': data})