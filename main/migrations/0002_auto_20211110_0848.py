from django.db import migrations


def forwards_func(apps, schema_editor):
    worker = apps.get_model("main", "Worker")
    db_alias = schema_editor.connection.alias
    worker.objects.using(db_alias).bulk_create([
        worker(pk="1", name="Dan"),
        worker(pk="2", name="Odet"),
        worker(pk="3", name="Gali"),
        worker(pk="4", name="Miri"),
    ])


def reverse_func(apps, schema_editor):
    worker = apps.get_model("main", "Worker")
    db_alias = schema_editor.connection.alias
    worker.objects.using(db_alias).filter(pk="1", name="Dan").delete()
    worker.objects.using(db_alias).filter(pk="2", name="Odet").delete()
    worker.objects.using(db_alias).filter(pk="3", name="Gali").delete()
    worker.objects.using(db_alias).filter(pk="4", name="Miri").delete()


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
