# Generated by Django 3.0.7 on 2020-08-18 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORMTest', '0003_auto_20200818_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='contact',
            field=models.IntegerField(max_length=20),
        ),
    ]
