from django.contrib import admin

from .models import City, SearchHistory


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'owm_city_id', 'owm_city_name', 'owm_country')
    search_fields = ('owm_city_name', 'owm_city_id')
    empty_value_display = '-пусто-'


class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'city', 'created_at')
    empty_value_display = '-пусто-'


admin.site.register(City, CityAdmin)
admin.site.register(SearchHistory, SearchHistoryAdmin)
