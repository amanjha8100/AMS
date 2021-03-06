# Generated by Django 3.1.7 on 2021-03-01 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20210301_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=64)),
                ('subj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.subject')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('roll', models.IntegerField()),
                ('date', models.DateField(blank=True)),
                ('sub', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.subject')),
                ('time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.time')),
            ],
        ),
    ]
