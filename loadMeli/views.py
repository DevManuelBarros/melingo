from django.shortcuts import render
from meli.meli import Meli
from django.http import HttpResponse, HttpResponseRedirect
from .serializers import LoginModelSerializer
from .models import LoginModel
 
 
 
def initial_login(request):
    meli = Meli()
    escritura = meli.auth_url_melingo()
    return HttpResponseRedirect(escritura)
 
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
        return HttpResponse("Nadinas")
    return HttpResponse("Se esta guardando")