# Generated by Django 3.0.7 on 2020-08-12 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ORMApp', '0002_auto_20200811_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='emp',
            new_name='Emp_Id',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='std',
            new_name='Student_Rank',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='rollNo',
            new_name='Rank',
        ),
    ]
