# Generated by Django 2.1.1 on 2018-09-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackingservice', '0005_auto_20180908_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='token_no',
            field=models.IntegerField(default=4126),
        ),
        migrations.AlterField(
            model_name='driver',
            name='token_no',
            field=models.IntegerField(default=7987),
        ),
        migrations.AlterField(
            model_name='user',
            name='token_no',
            field=models.IntegerField(default=3933),
        ),
    ]