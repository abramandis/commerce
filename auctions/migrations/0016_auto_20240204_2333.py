# Generated by Django 3.1.2 on 2024-02-04 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20240204_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('option1', 'TOYS'), ('option2', 'FASHION'), ('option3', 'FURNITURE'), ('option4', 'ELECTRONICS'), ('option5', 'OTHER')], max_length=100),
        ),
    ]