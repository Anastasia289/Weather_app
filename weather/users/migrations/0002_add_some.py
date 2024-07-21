from django.contrib.auth.hashers import make_password
from django.db import migrations


def add_users(apps, schema_editor):
    CustomUser = apps.get_model("users", "CustomUser")

    CustomUser.objects.get_or_create(
        username='admin',
        password=make_password('admin'),
        email='admin@admin.ru',
        is_superuser=True,
        is_staff=True
    )

    CustomUser.objects.get_or_create(
        username='vasya',
        password=make_password('zxc102938'),
        email='vasya@admin.ru',
        is_superuser=False,
        is_staff=True
    )
    CustomUser.objects.get_or_create(
        username='masha',
        password=make_password('mko091122'),
        email='masha@masha.ru',
        is_superuser=False,
        is_staff=True
    )

    CustomUser.objects.get_or_create(
        username='ivan',
        password=make_password('mkoivan22'),
        email='ivan@ivan.ru',
        is_superuser=False,
        is_staff=True
    )

    CustomUser.objects.get_or_create(
        username='daria',
        password=make_password('mko09daria'),
        email='daria@daria.ru',
        is_superuser=False,
        is_staff=True
    )


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_users),
    ]
