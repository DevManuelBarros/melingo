from django.db import migrations, models, transaction


def insertValues(apps, schema_editor):
    MeansModel = apps.get_model('meli', 'MeansModel')
    values = {('SYI','Sell your Item', 'Flujo de publicacion de ítem'),
              ('VIP', 'View Item Page', 'Vista de la publicación'),
             }
    for value in values:
        result = MeansModel.objects.filter(term=value[0])
        if len(result) == 0:
            with transaction.atomic():
                MeansModel.objects.create(term=value[0],means=value[1], description=value[2])

class Migration(migrations.Migration):

    initial = False

    dependencies = [
        ('meli', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insertValues, migrations.RunPython.noop)
    ]