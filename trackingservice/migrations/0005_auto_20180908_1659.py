# Generated by Django 2.1.1 on 2018-09-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackingservice', '0004_auto_20180908_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='token_no',
            field=models.IntegerField(default=3507),
        ),
        migrations.AlterField(
            model_name='driver',
            name='token_no',
            field=models.IntegerField(default=2628),
        ),
        migrations.AlterField(
            model_name='driverservice',
            name='stop_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='driverservice',
            name='stop_long',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='driverstatus',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token_no',
            field=models.IntegerField(default=8385),
        ),
    ]