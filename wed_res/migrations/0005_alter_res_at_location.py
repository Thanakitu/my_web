# Generated by Django 4.2.5 on 2023-11-08 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wed_res', '0004_alter_res_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='res',
            name='at_location',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
