# Generated by Django 2.0 on 2022-03-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_messagechat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagechat',
            name='receiver',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='messagechat',
            name='sender',
            field=models.IntegerField(),
        ),
    ]