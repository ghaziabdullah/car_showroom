# Generated by Django 4.2.3 on 2023-07-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0007_remove_features_car_features_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='designation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]