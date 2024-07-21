import json
import os

import requests
from django.shortcuts import get_object_or_404, render
# from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import permission_classes  # api_view,
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from check_weather.models import City, SearchHistory
from users.models import CustomUser

from .serializers import (CityGetSerializer, CustomUserSerializer,
                          SearchHistorySerializer)


class CustomUserViewSet(UserViewSet):
    """Вьюсет для пользователей."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'post',]


class CityViewSet(viewsets.ModelViewSet):
    """Вьюсет для городов"""

    queryset = City.objects.all()
    serializer_class = CityGetSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('owm_city_name', )
    http_method_names = ['get',]


class SearchViewSet(viewsets.ModelViewSet):
    """Вьюсет для городов"""

    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ('owm_city_name', )
    http_method_names = ['get',]


def index(request):
    data = {}
    if request.user.is_authenticated:
        data['search_history'] = get_search_history(request,)
    if request.method == "POST":
        cit = request.POST.get('city')
        try:
            city = get_object_or_404(City, owm_city_name=cit)
        except Exception:
            print("Город не найден")
        try:
            data = get_weather(city.owm_city_id, data)
        except Exception:
            print("Что-то погоду не получить")
        try:
            SearchHistory_create(city, request)
            data['search_history'] = get_search_history(request,)
        except Exception:
            print("История не сохраняется")
    return render(request, "index.html", {'data': data},)


def get_weather(city, data):
    """Получение погоды по городу"""
    API_KEY = os.getenv('API_KEY', default='73d4eb76b4a0c408fd16f3acc5cb28f4')
    try:
        response = requests.get(
            url=('https://api.openweathermap.org/data/2.5/'
                 f'weather?id={city}&appid={API_KEY}&units=metric')
            )
        response.raise_for_status()
        list_of_data = response.json()
        weather_data = list_of_data['weather']
        weather, *w2 = weather_data
        data["city"] = city,
        data["city_name"] = str(list_of_data['name']),
        data["country_code"] = str(list_of_data['sys']['country'])
        data['coordinate'] = (f'{list_of_data['coord']['lon']}'
                              f'{list_of_data['coord']['lat']}')
        data['weather'] = f"{weather['main']}, {weather['description']}"
        data['temp'] = (f'{list_of_data['main']['temp']}',
                        f'(min: {list_of_data['main']['temp_min']} - ',
                        f'(max: {list_of_data['main']['temp_max']})')
        data['feels_like'] = str(list_of_data['main']['feels_like'])
        data['pressure'] = str(list_of_data['main']['pressure'])
        data['humidity'] = str(list_of_data['main']['humidity'])

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")
    except json.JSONDecodeError as json_err:
        print(f"JSON decode error: {json_err}")
    return (data)


@permission_classes([IsAuthenticated])
def get_search_history(request):
    """Выводим историю запросов для авторизованных пользователей."""
    data = {}
    searchhistory = SearchHistory.objects.filter(
        user=request.user).all()
    for history in searchhistory:
        if history.city.owm_city_name not in data:
            data[history.city.owm_city_name] = 1
        else:
            data[history.city.owm_city_name] += 1
    return (data)


@permission_classes([IsAuthenticated])
def SearchHistory_create(city, request):
    serializer = SearchHistorySerializer(
        data={
            'user': request.user.id,
            'city': city.id,
            },
        context={'request': request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response('Город добавлен в историю поиска',
                    status=status.HTTP_201_CREATED)
