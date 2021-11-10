from django.db import migrations


def forwards_func(apps, schema_editor):
    project = apps.get_model("main", "Project")
    db_alias = schema_editor.connection.alias
    project.objects.using(db_alias).bulk_create([
        project(pk="1", name="Simple"),
        project(pk="2", name="Cynerio"),
        project(pk="3", name="Test")
    ])


def reverse_func(apps, schema_editor):
    project = apps.get_model("main", "Project")
    db_alias = schema_editor.connection.alias
    project.objects.using(db_alias).filter(pk="1", name="Simple").delete()
    project.objects.using(db_alias).filter(pk="2", name="Cynerio").delete()
    project.objects.using(db_alias).filter(pk="3", name="Test").delete()


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_auto_20211110_0848'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
