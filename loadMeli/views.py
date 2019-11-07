from django.shortcuts import render
from meli.meli import Meli
from django.http import HttpResponse, HttpResponseRedirect
from .serializers import LoginModelSerializer
from .models import LoginModel
from django.contrib.auth.decorators import login_required
from django.urls import reverse



@login_required(redirect_field_name='login')
def initial_login(request):
    meli = Meli()
    escritura = meli.auth_url_melingo()
    if "auth.mercadolibre.com" in escritura:
        return HttpResponseRedirect(escritura)
    else:
        return HttpResponse("Modulo Ingresado")
    
@login_required(redirect_field_name='login')
def login(request):
    code = request.GET.get('code', '')
    if code:
        meli = Meli()
        response = meli.authorize_melingo(code)
        print(type(response))
        tmpInstance = LoginModel.objects.all().last()
        tmpSerializer  = LoginModelSerializer()
        tmpSerializer.update(tmpInstance, response)
    else:
        return HttpResponseRedirect(reverse('initial_login'))
    return HttpResponseRedirect(reverse('profile'))

def profile(request):
    meli = Meli(charge_data=True)
    response = meli.get('/users/me', params={'access_token':meli.access_token})
    print(response.content)
    return HttpResponse(response.content)


