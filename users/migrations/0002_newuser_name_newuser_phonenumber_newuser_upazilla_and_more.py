# Generated by Django 4.0.2 on 2022-02-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='name',
            field=models.CharField(default='alvi hasan', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newuser',
            name='phoneNumber',
            field=models.CharField(default='-1', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newuser',
            name='upazilla',
            field=models.CharField(default='comilla', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newuser',
            name='zilla',
            field=models.CharField(default='sreekamta', max_length=20),
            preserve_default=False,
        ),
    ]
