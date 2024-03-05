# Generated by Django 5.0.2 on 2024-03-05 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0003_blogmodel_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='formModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]