# Generated by Django 3.1.7 on 2021-06-04 13:17

import Home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_auto_20210305_0305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['roll']},
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='time',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(validators=[Home.models.date_valid]),
        ),
    ]
