# Generated by Django 2.0.6 on 2019-11-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0003_auto_20191124_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='nickname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='id别称'),
        ),
    ]
