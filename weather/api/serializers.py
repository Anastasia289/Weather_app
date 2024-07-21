from check_weather.models import City, SearchHistory
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
# from rest_framework.fields import SerializerMethodField
from users.models import CustomUser


class CustomUserSerializer(UserSerializer):
    """Сериализатор для управления пользователями."""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password',)


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя."""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', )


class CityGetSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра городов."""

    class Meta:
        model = City
        fields = ('id', 'owm_city_id', 'owm_city_name', )


class CityChangeSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и редактирования городов."""

    class Meta:
        model = City
        fields = '__all__'


class SearchHistorySerializer(serializers.ModelSerializer):
    """Сериализатор истории поиска."""

    class Meta:
        model = SearchHistory
        fields = ('id', 'city', 'user', 'created_at')
