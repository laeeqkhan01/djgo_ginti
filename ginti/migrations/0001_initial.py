# Generated by Django 3.0.8 on 2020-09-26 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdadTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('sqr', models.IntegerField()),
                ('sound', models.CharField(max_length=16)),
            ],
        ),
    ]
