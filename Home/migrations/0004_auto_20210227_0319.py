# Generated by Django 3.1.7 on 2021-02-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_attendanceclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendanceclass',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
