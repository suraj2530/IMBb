# Generated by Django 3.2.7 on 2021-10-03 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0009_auto_20211002_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='avg_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='review',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
