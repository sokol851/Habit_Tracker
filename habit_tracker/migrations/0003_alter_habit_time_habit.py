# Generated by Django 4.2.16 on 2024-11-06 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0002_alter_habit_time_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time_habit',
            field=models.DurationField(verbose_name='Время на выполнение'),
        ),
    ]
