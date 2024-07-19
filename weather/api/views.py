from django.shortcuts import render
import requests
import json
import os
from dotenv import load_dotenv


def index(request):
    data = {}  # Initialize data as empty for both GET and POST requests
    API_KEY = os.getenv('API_KEY', default='73d4eb76b4a0c408fd16f3acc5cb28f4')

    if request.method == "POST":
        city = request.POST.get('city')
        if city:
            try:
                response = requests.get(
                    url=f'https://api.openweathermap.org/data/2.5/weather?id={city}&appid={API_KEY}&units=metric'
                )
                response.raise_for_status()  # Raise an error for bad status codes
                list_of_data = response.json()
                w = list_of_data['weather']
                weather, *w2 = w

                data = {
                    "city": city,  # Add the city name to the data dictionary
                    "city_name": str(list_of_data['name']),
                    "country_code": str(list_of_data['sys']['country']),
                    'coordinate': f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
                    'weather': f"{weather['main']}, {weather['description']}",
                    'temp': f"{list_of_data['main']['temp']} (min: {list_of_data['main']['temp_min']} - (max: {list_of_data['main']['temp_max']})",
                    'feels_like': str(list_of_data['main']['feels_like']),
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
