# Generated by Django 3.0.7 on 2020-09-29 05:27

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
                ('email', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('month', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestApp.Emp')),
            ],
        ),
    ]
