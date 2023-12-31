# Generated by Django 4.2.5 on 2023-10-30 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wed_location', '0001_initial'),
        ('wed_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavoriteLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.SmallIntegerField(choices=[(1, '1ดาว'), (2, '2ดาว'), (3, '3ดาว'), (4, '4ดาว'), (5, '5ดาว')], default=1)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorited_user_pivot_set', to='wed_location.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_location_pivot_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='favorite_location_set',
            field=models.ManyToManyField(related_name='favorited_user_set', through='wed_users.UserFavoriteLocation', to='wed_location.location'),
        ),
    ]
