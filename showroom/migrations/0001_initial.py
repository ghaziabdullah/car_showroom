# Generated by Django 4.2.3 on 2023-07-28 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('ChasisNo', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EngineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShowRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('Brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='showroom.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('engineNo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='showroom.car')),
                ('engineModel', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='showroom.enginemodel')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='Model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='showroom.model'),
        ),
        migrations.AddField(
            model_name='brand',
            name='ShowRoom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='showroom.showroom'),
        ),
    ]
