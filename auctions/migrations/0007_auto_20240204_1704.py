# Generated by Django 3.1.2 on 2024-02-04 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20240204_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='highest_bid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winning_bid', to='auctions.bid'),
        ),
    ]
