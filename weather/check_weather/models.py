from django.contrib.auth import get_user_model
from django.db import models

from weather.constants import MAX_CHAR_LENGTH

User = get_user_model()


class City(models.Model):
    """Города."""
    owm_city_id = models.CharField('Id города', max_length=MAX_CHAR_LENGTH)
    owm_city_name = models.CharField('Название города',
                                     max_length=MAX_CHAR_LENGTH)
    owm_latitude = models.FloatField('Широта')
    owm_longitude = models.FloatField('Долгота')
    owm_country = models.CharField('Страна',
                                   max_length=MAX_CHAR_LENGTH)
    locality_short = models.CharField('Место коротко',
                                      max_length=MAX_CHAR_LENGTH)
    locality_long = models.CharField('Место',
                                     max_length=MAX_CHAR_LENGTH)
    admin_level_1_short = models.CharField(max_length=MAX_CHAR_LENGTH)
    admin_level_1_long = models.CharField(max_length=MAX_CHAR_LENGTH)
    admin_level_2_short = models.CharField(max_length=MAX_CHAR_LENGTH)
    admin_level_2_long = models.CharField(max_length=MAX_CHAR_LENGTH)
    admin_level_3_short = models.CharField(max_length=MAX_CHAR_LENGTH)
    admin_level_3_long = models.CharField(max_length=MAX_CHAR_LENGTH)
    admin_level_4_short = models.CharField(max_length=MAX_CHAR_LENGTH)
    admin_level_4_long = models.CharField(max_length=MAX_CHAR_LENGTH)
    admin_level_5_short = models.CharField(max_length=MAX_CHAR_LENGTH)
    admin_level_5_long = models.CharField(max_length=MAX_CHAR_LENGTH)
    country_short = models.CharField(max_length=MAX_CHAR_LENGTH)
    country_long = models.CharField(max_length=MAX_CHAR_LENGTH)
    postal_code = models.CharField(max_length=MAX_CHAR_LENGTH)

    class Meta:
        verbose_name = ("Город")
        verbose_name_plural = ("Города")
        ordering = ['id']

    def __str__(self):
        return self.owm_city_id


class SearchHistory(models.Model):
    """Список запросов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='client',
        verbose_name='пользователь',)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='searched_city',
        verbose_name='город',)
    created_at = models.DateTimeField(verbose_name='Время запроса',
                                      auto_now_add=True)

    class Meta:
        verbose_name = ("Запрошенный город")
        verbose_name_plural = ("Запрошенные города")
        ordering = ['id']

    def __str__(self):
        return f'{self.user} искал {self.city}'
