# Generated by Django 2.2.6 on 2019-10-30 03:50
 
from django.db import migrations, models
 
 
class Migration(migrations.Migration):
 
    dependencies = [
        ('loadMeli', '0002_insertvalues'),
    ]
    operations = [
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=128)),
                ('token_type', models.CharField(max_length=128)),
                ('expires_in', models.IntegerField()),
                ('scope', models.CharField(max_length=128)),
                ('refresh_token', models.CharField(max_length=128)),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
