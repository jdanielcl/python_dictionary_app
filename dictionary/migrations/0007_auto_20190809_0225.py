# Generated by Django 2.2.4 on 2019-08-09 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0006_auto_20190808_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempts',
            name='attempts',
            field=models.IntegerField(default=0),
        ),
    ]