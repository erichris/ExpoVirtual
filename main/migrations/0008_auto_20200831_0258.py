# Generated by Django 3.0.5 on 2020-08-31 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200831_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='related_expo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.Expo'),
        ),
        migrations.AddField(
            model_name='platformuser',
            name='first_login',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.VisitantRegister'),
        ),
    ]
