from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.shortcuts import render

from .views import index, CustomUserViewSet, CityViewSet

app_name = "api"
router_v1 = DefaultRouter()

router_v1.register('users', CustomUserViewSet, basename='users')
router_v1.register('city', CityViewSet, basename='city')


urlpatterns = [
    path('', index),
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    
    # path('search/', search_city_name, name='search_city_name'),
]
