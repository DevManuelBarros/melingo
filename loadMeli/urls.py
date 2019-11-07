from django.urls import path
from .views import initial_login, login, profile
urlpatterns = [
    path('', initial_login, name='initial_login'),
    path('melingo/', login, name='login'),
    path('melingo/profile', profile, name='profile'),
]
