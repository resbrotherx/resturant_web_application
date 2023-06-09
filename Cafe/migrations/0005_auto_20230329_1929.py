# Generated by Django 3.2.18 on 2023-03-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cafe', '0004_auto_20230318_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='african_soup',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='break_fast',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='dessert',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='grills',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='pasta_and_nodles',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='pepper_soup',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='rice',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='salad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='sandwich_and_burgers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='sauce_and_stew',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='side',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='starters',
            field=models.BooleanField(default=False),
        ),
    ]
