from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CityViewSet, CustomUserViewSet, SearchViewSet, index

app_name = "api"
router_v1 = DefaultRouter()

router_v1.register('users', CustomUserViewSet, basename='users')
router_v1.register('city', CityViewSet, basename='city')
router_v1.register('search', SearchViewSet, basename='search')


urlpatterns = [
    path('', index),
    path('v1/', include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
