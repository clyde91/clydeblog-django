# Generated by Django 3.0.5 on 2021-03-11 01:57

import ckeditor_uploader.fields
import common_func.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Private',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '私密日志',
                'ordering': ['-created_time'],
            },
            bases=(models.Model, common_func.models.ReadnumMethod),
        ),
    ]
