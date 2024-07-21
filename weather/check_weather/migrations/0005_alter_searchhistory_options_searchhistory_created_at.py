# Generated by Django 4.2.9 on 2024-07-20 10:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('check_weather', '0004_searchhistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchhistory',
            options={'ordering': ['id'], 'verbose_name': 'Запрошенный город', 'verbose_name_plural': 'Запрошенные города'},
        ),
        migrations.AddField(
            model_name='searchhistory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время запроса'),
            preserve_default=False,
        ),
    ]
