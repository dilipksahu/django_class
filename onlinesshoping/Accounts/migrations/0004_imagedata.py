# Generated by Django 3.0.7 on 2020-09-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20200923_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgname', models.CharField(max_length=30)),
                ('img', models.ImageField(default='', upload_to='imges')),
            ],
        ),
    ]