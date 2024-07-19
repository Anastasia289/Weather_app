# Generated by Django 4.2.9 on 2024-07-18 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owm_city_name', models.CharField(max_length=150, verbose_name='Название города')),
                ('owm_latitude', models.FloatField(verbose_name='Широта')),
                ('owm_longitude', models.FloatField(verbose_name='Долгота')),
                ('owm_country', models.CharField(max_length=150, verbose_name='Страна')),
                ('locality_short', models.CharField(max_length=150, verbose_name='Место коротко')),
                ('locality_long', models.CharField(max_length=150, verbose_name='Место')),
                ('admin_level_1_short', models.CharField(max_length=150)),
                ('admin_level_1_long', models.CharField(max_length=150)),
                ('admin_level_2_short', models.CharField(max_length=150)),
                ('admin_level_2_long', models.CharField(max_length=150)),
                ('admin_level_3_short', models.CharField(max_length=150)),
                ('admin_level_3_long', models.CharField(max_length=150)),
                ('admin_level_4_short', models.CharField(max_length=150)),
                ('admin_level_4_long', models.CharField(max_length=150)),
                ('admin_level_5_short', models.CharField(max_length=150)),
                ('admin_level_5_long', models.CharField(max_length=150)),
                ('country_short', models.CharField(max_length=150)),
                ('country_long', models.CharField(max_length=150)),
                ('postal_code', models.IntegerField(verbose_name='Почтовый индекс')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['id'],
            },
        ),
    ]
