import json

from django.core.management import BaseCommand

from check_weather.models import City


class Command(BaseCommand):
    """Команда для чтения json файла и добавления информации в базу."""

    help = 'импорт данных из json'

    def handle(self, *args, **options):
        with open('data/owm_city_list.json',
                  encoding='utf-8',) as data:
            cities = json.loads(data.read())
            try:
                City.objects.bulk_create([
                    City(**city)
                    for city in cities], ignore_conflicts=True)
            except Exception as error:
                self.stderr.write(f'Упс, загрузка не удалась: {error}')
            self.stdout.write(self.style.SUCCESS('Данные загружены'))

# python manage.py load_cities
# docker-compose exec backend python manage.py load_cities
