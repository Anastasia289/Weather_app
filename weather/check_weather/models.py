from django.db import models
from django.db import models

from weather.constants import MAX_CHAR_LENGTH


class City(models.Model):
    """Города как в базе."""
    owm_city_id = models.IntegerField('Id города')
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
