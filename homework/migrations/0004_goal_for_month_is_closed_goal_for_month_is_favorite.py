# Generated by Django 4.2.6 on 2023-12-09 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_habits'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal_for_month',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='goal_for_month',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
