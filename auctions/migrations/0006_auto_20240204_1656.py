# Generated by Django 3.1.2 on 2024-02-04 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20240204_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='user',
            new_name='created_by',
        ),
    ]
