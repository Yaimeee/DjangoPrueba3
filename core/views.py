from core.forms import VehiculoForm
from django import forms
from django.shortcuts import render


# Create your views here.


def index(request):

    return render(request, 'core/index.html')


def Contactos(request):

    return render(request, 'Contactos/index.html')


def Cotizar(request):

    return render(request, 'Cotizar/index.html')


def Trabajos(request):

    return render(request, 'core/Trabajos.html')
