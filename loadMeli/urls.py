from django.urls import path
from .views import initial_login, login, profile
urlpatterns = [
    path('initial_login/', initial_login, name='initial_login'),
    path('', login, name='login'),
    path('profile/', profile, name='profile'),
]
