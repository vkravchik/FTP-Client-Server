# Generated by Django 3.0.1 on 2019-12-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('secure', models.BooleanField()),
            ],
        ),
    ]
