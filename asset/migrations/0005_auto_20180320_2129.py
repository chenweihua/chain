# Generated by Django 2.0.3 on 2018-03-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_auto_20180320_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='region',
            field=models.CharField(choices=[('1', '华北2'), ('2', '香港'), ('3', '东京'), ('4', '美国')], max_length=128, verbose_name='区域'),
        ),
    ]
