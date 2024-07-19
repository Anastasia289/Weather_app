from django.shortcuts import render
import requests
import json
import os 
from dotenv import load_dotenv
from check_weather.models import City
from users.models import CustomUser
from datetime import datetime
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from users.models import CustomUser
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (CustomUserSerializer, CityGetSerializer, CityChangeSerializer,
                          )
from .permissions import IsAdminOrReadOnly
from .filters import CityFilter
from django.views.generic import TemplateView, ListView


class CustomUserViewSet(UserViewSet):
    """Позволяет просматривать список всех пользователей,
    и свою страницу, а также регистрироваться. Вместе с информацией
    о пользователе получаем его историю аренды велосипедов."""

    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, ]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^email',)
    ordering_fields = ('id', )
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'post',]


class CityViewSet(UserViewSet):
    """Вьюсет для городов"""

    queryset = City.objects.select_related('owm_city_name')
    # permission_classes = (IsAuthenticatedOrReadOnly,
    #                       IsAdminOrReadOnly,)
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CityFilter
    search_fields = ('^owm_city_name', '^owm_city_id',)
    ordering_fields = ('owm_city_name', 'owm_city_id',)
    http_method_names = ['get', 'post',]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CityGetSerializer
        return CityChangeSerializer




def index(request):
    data = {}  # Initialize data as empty for both GET and POST requests
    # API_KEY = os.getenv('API_KEY', default='73d4eb76b4a0c408fd16f3acc5cb28f4')
    cities = City.objects.all()
    if request.method == "POST":
        cit = request.POST.get('city')
        # city = City.objects.filter(owm_city_name=cit)
        city = get_object_or_404(City, owm_city_name=cit)
        data = get_weather(city.owm_city_id)

    return render(request, "index.html", {'data': data})





def get_weather(city):
    """Получение погоды по городу"""
    API_KEY = os.getenv('API_KEY', default='73d4eb76b4a0c408fd16f3acc5cb28f4')
    try:
        response = requests.get(
            url=f'https://api.openweathermap.org/data/2.5/weather?id={city}&appid={API_KEY}&units=metric'
            )
        response.raise_for_status()  # Raise an error for bad status codes
        list_of_data = response.json()
        weather_data = list_of_data['weather']
        weather, *w2 = weather_data
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
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")
    except json.JSONDecodeError as json_err:
        print(f"JSON decode error: {json_err}")
    return(data)


class SearchResultsView(ListView):
    model = City
    template_name = 'city.html'
