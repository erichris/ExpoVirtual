# Generated by Django 3.0.5 on 2020-08-25 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expo',
            name='banner',
        ),
        migrations.AddField(
            model_name='expo',
            name='Calendario',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='expo',
            name='Hall1',
            field=models.TextField(default='default'),
        ),
        migrations.AddField(
            model_name='expo',
            name='Hall2',
            field=models.TextField(default='default'),
        ),
        migrations.AddField(
            model_name='expo',
            name='TripticoPage1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='expo',
            name='TripticoPage10',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='expo',
            name='TripticoPage2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='expo',
            name='TripticoPage3',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='expo',
            name='TripticoPage4',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='expo',
            name='TripticoPage5',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='expo',
            name='TripticoPage6',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='expo',
            name='TripticoPage7',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='expo',
            name='TripticoPage8',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='expo',
            name='TripticoPage9',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='expo',
            name='bannerA',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='expo',
            name='bannerB',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='StandDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standType', models.IntegerField()),
                ('color1', models.CharField(max_length=50)),
                ('color2', models.CharField(max_length=50)),
                ('color3', models.CharField(max_length=50)),
                ('related_stand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Stand')),
            ],
            options={
                'verbose_name': 'StandDesign',
                'verbose_name_plural': 'StandDesigns',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='default')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.Expo')),
            ],
        ),
        migrations.CreateModel(
            name='ExpoDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_expo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Expo')),
            ],
            options={
                'verbose_name': 'StandDesign',
                'verbose_name_plural': 'StandDesigns',
            },
        ),
    ]
