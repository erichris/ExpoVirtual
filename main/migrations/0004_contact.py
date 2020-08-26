# Generated by Django 3.0.5 on 2020-08-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200825_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='', max_length=80, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=80, null=True)),
                ('telefono', models.CharField(blank=True, default='', max_length=80, null=True)),
                ('mensaje', models.TextField(blank=True, default='', null=True)),
                ('interes', models.CharField(blank=True, default='', max_length=40, null=True)),
            ],
        ),
    ]
