# Generated by Django 3.1.7 on 2021-03-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude01', models.CharField(max_length=4)),
                ('latitude01', models.CharField(max_length=4)),
                ('longitude02', models.CharField(max_length=4)),
                ('latitude02', models.CharField(max_length=4)),
            ],
        ),
    ]
