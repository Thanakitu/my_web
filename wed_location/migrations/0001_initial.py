# Generated by Django 4.2.5 on 2023-10-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('is_Recommend', models.BooleanField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('googlemap', models.URLField(blank=True, max_length=500)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('image_a', models.CharField(blank=True, max_length=50, null=True)),
                ('image_b', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
