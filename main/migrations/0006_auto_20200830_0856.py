# Generated by Django 3.0.5 on 2020-08-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200827_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platformuser',
            name='user_expo',
            field=models.ManyToManyField(blank=True, to='main.Expo'),
        ),
        migrations.AlterField(
            model_name='platformuser',
            name='user_stand',
            field=models.ManyToManyField(blank=True, to='main.Stand'),
        ),
    ]
