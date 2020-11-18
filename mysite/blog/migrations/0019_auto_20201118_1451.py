# Generated by Django 3.1.2 on 2020-11-18 09:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20201117_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 18, 9, 21, 3, 987774, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 18, 9, 21, 3, 987774, tzinfo=utc)),
        ),
    ]
