# Generated by Django 3.2.9 on 2021-11-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211110_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklog',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End work in'),
        ),
    ]
