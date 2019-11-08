from django.shortcuts import render
from meli.meli import Meli
from django.http import HttpResponse, HttpResponseRedirect
from .serializers import LoginModelSerializer
from .models import LoginModel
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.forms.models import model_to_dict


#www.mercadolibre.com/jms/mla/lgz/logout?go=http%3A%2F

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
        tmpInstance = LoginModel.objects.all().last()
        tmpSerializer  = LoginModelSerializer()
        tmpSerializer.update(tmpInstance, response)
    else:
        return HttpResponseRedirect(reverse('initial_login'))
    return HttpResponseRedirect(reverse('profile'))

def profile(request):
    meli = Meli(charge_data=True)
    context = meli.get('/users/me', params={'access_token':meli.access_token})
    return render(request, 'loadMeli/profile.html', {'context' : context.json()})


