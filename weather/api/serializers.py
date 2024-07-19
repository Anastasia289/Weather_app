from check_weather.models import City
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from users.models import CustomUser


class CustomUserSerializer(UserSerializer):
    """Сериализатор для управления пользователями."""

    # earch_history = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email',) # 'search_history',)

    # def get_search_history(self, obj):
    #     search_history = Search_history.objects.filter(user_id=obj).all()
    #     return SearchHistorySerializer(rented_bicycles, many=True).data


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя."""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', )


class CityGetSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра городов."""

    class Meta:
        model = City
        fields = ('owm_city_id', 'owm_city_name', )


class CityChangeSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и редактирования городов."""

    class Meta:
        model = City
        fields = '__all__'
