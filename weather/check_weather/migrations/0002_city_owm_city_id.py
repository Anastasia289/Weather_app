# Generated by Django 4.2.9 on 2024-07-18 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='owm_city_id',
            field=models.IntegerField(default=0, verbose_name='Id города'),
            preserve_default=False,
        ),
    ]