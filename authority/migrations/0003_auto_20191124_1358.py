# Generated by Django 2.0.6 on 2019-11-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0002_permission_is_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='请求路径'),
        ),
    ]
