from django.db import migrations, models, transaction


def insertValue(apps, schema_editor):
    LoginModel = apps.get_model('loadMeli', 'LoginModel')
    with transaction.atomic():
        LoginModel.objects.create(access_token='AccessToken',
                                  token_type='TokenType', 
                                  expires_in = 0,
                                  scope='scope',
                                  refresh_token='RefreshToken')

class Migration(migrations.Migration):

    initial = False

    dependencies = [
        ('loadMeli', '0003_loginmodel'),
    ]

    operations = [
        migrations.RunPython(insertValue, migrations.RunPython.noop)
    ]