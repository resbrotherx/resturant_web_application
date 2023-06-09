# Generated by Django 3.2.18 on 2023-04-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cafe', '0008_auto_20230404_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default='873, Ozumba Mbadiwe , Victoria Island, Lagos', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='email',
            field=models.EmailField(default='Slipperylounge11@gmail.com', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='new',
            field=models.BooleanField(default=False),
        ),
    ]
