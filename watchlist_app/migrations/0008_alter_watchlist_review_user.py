# Generated by Django 3.2.7 on 2021-10-02 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watchlist_app', '0007_watchlist_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='review_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]