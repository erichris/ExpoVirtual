# Generated by Django 3.0.5 on 2020-09-21 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200920_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='receiver',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='sender',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
