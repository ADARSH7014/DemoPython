# Generated by Django 4.1.4 on 2023-01-05 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-02-02'),
            preserve_default=False,
        ),
    ]
