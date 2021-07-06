from django.urls import path
from .views import Contactos, Cotizar, Trabajos, index,

urlpatterns = [
    path('Contactos', Contactos, name="Contactos"),
    path('Cotizar', Cotizar, name="Cotizar"),
    path('index', index, name="index"),
    path('Trabajos', Trabajos, name="Trabajos"),

]
