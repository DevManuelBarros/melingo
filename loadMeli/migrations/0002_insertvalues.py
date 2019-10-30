from django.db import migrations, models, transaction


def insertValues(apps, schema_editor):
    MeansModel = apps.get_model('loadMeli', 'MeansModel')
    values = {('SYI','Sell your Item', 'Flujo de publicacion de ítem'),
            ('VIP', 'View Item Page', 'Vista de la publicación'),
            ('ME2', 'MercadoEnvíos', 'Plataforma de Logística'),
            ('MP', 'MercadoPago', 'Pasarela de pagos Online'),
            ('Meli', 'MercadoLibre', 'Pasarela de pagos Online'),
            ('MLA', 'MercadoLibre Argentina', 'Id identificardor del site para Argentina'),
            ('MLB', 'MercadoLibre Brasil', 'Id identificardor del site para Brasil'),
            ('Variations', 'Variación Estandar de MercadoLibre', 'Pertenecen a una categoría como por ejemplo: Talle y Color en Ropa y Accesorios'),
            ('Core', 'Referencia al Markplace', 'Core Business de MercadoLibre, hace referencia al flujo de compra y venta dentro de la plataforma'),
            ('clasi', 'Referencia a los clasificados', 'Inmuebles, Automotores, servicios'),
            ('PHQLV', 'Publica hasta que lo vendas', ''),
            ('MShops', 'MercadoShops', 'Plataforma de Tienda Web'),
            ('To', 'Tienda Oficial', ''),
            ('Upgrade', 'Aumentar Exposición', ''),
            ('Downgrade', 'Dismunuir Exposición', ''),
            }
    for value in values:
        result = MeansModel.objects.filter(term=value[0])
        if len(result) == 0:
            with transaction.atomic():
                MeansModel.objects.create(term=value[0],means=value[1], description=value[2])

class Migration(migrations.Migration):

    initial = False

    dependencies = [
        ('loadMeli', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insertValues, migrations.RunPython.noop)
    ]