# Generated by Django 3.2.7 on 2021-10-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0010_auto_20211003_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='avg_rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='number_rating',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]