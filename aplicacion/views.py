from django.http import HttpResponse
from django.template import *
from django.shortcuts import render
from aplicacion.models import alumnos, profesores

# Create your views here.
def index_bootstrap(request):
    return render(request, "index.html")


def formulario_alumnos(request):

    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        app = alumnos(nombre=nombre, apellido=apellido)
        app.save()
        return render(request, "formcompleto.html")

    return render(request, "alumnos.html")


def formulario_profesores(request):

    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        especialidad = request.POST["especialidad"]
        email = request.POST["email"]
        app = profesores(nombre=nombre, apellido=apellido, especialidad=especialidad, email=email)
        app.save()
        return render(request, "formcompleto.html")

    return render(request, "profesores.html")