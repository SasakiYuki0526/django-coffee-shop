# Generated by Django 3.2.9 on 2021-12-20 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffees', '0002_auto_20211206_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='coffee',
            name='update_at',
        ),
        migrations.RemoveField(
            model_name='grinding',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='grinding',
            name='update_at',
        ),
    ]
