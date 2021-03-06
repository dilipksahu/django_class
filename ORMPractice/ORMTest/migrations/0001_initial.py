# Generated by Django 3.0.7 on 2020-08-18 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('age', models.IntegerField()),
                ('cname', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Emp',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('stream', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('month', models.CharField(max_length=15)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ORMTest.Emp')),
                ('std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ORMTest.Student')),
            ],
            options={
                'db_table': 'Account',
            },
        ),
    ]
