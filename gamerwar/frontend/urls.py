from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Définissez la vue de votre page d'accueil
]
