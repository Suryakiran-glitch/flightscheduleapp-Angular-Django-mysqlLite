# Generated by Django 3.1.6 on 2021-02-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=200)),
                ('flight_no', models.CharField(max_length=50)),
                ('trip_type', models.CharField(max_length=50)),
                ('departure_airport', models.CharField(max_length=50)),
                ('arrival_airport', models.CharField(max_length=50)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
            ],
        ),
    ]
