# Generated by Django 3.0.5 on 2021-02-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210127_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='descriptison',
            field=models.CharField(blank=True, max_length=200, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='article',
            name='keywords',
            field=models.CharField(blank=True, max_length=100, verbose_name='关键词'),
        ),
    ]
