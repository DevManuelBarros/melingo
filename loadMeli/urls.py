from django.urls import path
from .views import initial_login, login
urlpatterns = [
    path('', initial_login, name='initial_login'),
    path('melingo/', login, name='login')
]
