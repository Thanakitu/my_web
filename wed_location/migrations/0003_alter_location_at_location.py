# Generated by Django 4.2.5 on 2023-11-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wed_location', '0002_location_at_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='at_location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]