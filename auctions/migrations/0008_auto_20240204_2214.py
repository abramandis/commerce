# Generated by Django 3.1.2 on 2024-02-04 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20240204_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='highest_bid',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=10),
        ),
    ]
