from django.shortcuts import render
from meli.meli import Meli
from django.http import HttpResponse, HttpResponseRedirect

def initial_login(request):
    meli = Meli()
    escritura = meli.auth_url_melingo()
    return HttpResponseRedirect(escritura)

def login(request):
    code = request.GET.get('code', '')
    if code:
        meli = Meli()
        access_token = meli.authorize_melingo(code)
    print(access_token)
    return HttpResponse(access_token)