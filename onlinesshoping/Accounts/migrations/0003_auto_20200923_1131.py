# Generated by Django 3.0.7 on 2020-09-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_placeorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeorder',
            name='status',
            field=models.CharField(default='Processing', max_length=30),
        ),
    ]
