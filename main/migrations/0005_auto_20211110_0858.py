# Generated by Django 3.2.9 on 2021-11-10 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_worklog_end_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worklog',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='worklog',
            old_name='worker_id',
            new_name='worker',
        ),
    ]
