# Generated by Django 4.2.3 on 2023-07-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0003_drinkscategory_drinks_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('guest_count', models.IntegerField()),
                ('reservation_time', models.DateField(auto_now=True)),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
    ]
