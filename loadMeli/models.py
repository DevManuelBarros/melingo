from django.db import models
 
"""
saco la App ID de aca: https://developers.mercadolibre.com.ar/devcenter/edit-app/3597278841256527
y la secret key.
 
aqui se obtiene los datos con el App Id:
https://developers.mercadolibre.com.ar/es_ar/autenticacion-y-autorizacion/#obtener_token
 
"""
 
class MeansModel(models.Model):
    term = models.CharField(max_length=128, blank=False, null=False, unique=True)
    means = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(null=True)
    def __str__(self):
        return self.term
 
class loginModel(models.Model):
    access_token = models.CharField(max_length=128, blank=False, null=False)
    token_type = models.CharField(max_length=128)
    expires_in = models.IntegerField()
    scope = models.CharField(max_length=128)
    refresh_token = models.CharField(max_length=128)
