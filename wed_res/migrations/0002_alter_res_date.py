# Generated by Django 4.2.5 on 2023-11-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wed_res', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='res',
            name='date',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
