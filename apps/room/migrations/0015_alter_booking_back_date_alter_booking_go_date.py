# Generated by Django 4.1.3 on 2022-11-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0014_alter_booking_back_date_alter_booking_go_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='back_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='go_date',
            field=models.DateField(),
        ),
    ]
