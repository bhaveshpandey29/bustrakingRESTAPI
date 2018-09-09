# Generated by Django 2.1.1 on 2018-09-08 09:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('token_no', models.IntegerField(default=8514)),
                ('profile_pic', models.ImageField(upload_to='user/profile/pic')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=10)),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('token_no', models.IntegerField(default=6761)),
                ('profile_pic', models.ImageField(upload_to='user/profile/pic')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
