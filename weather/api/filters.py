from django_filters import rest_framework as filters
from check_weather.models import City


class CityFilter(filters.FilterSet):
    owm_city_id = filters.CharFilter(field_name='owm_city_id__slug')
    owm_city_name = filters.CharFilter(field_name='owm_city_name__slug')

    class Meta:
        model = City
        fields = ['owm_city_id', 'owm_city_name',]
