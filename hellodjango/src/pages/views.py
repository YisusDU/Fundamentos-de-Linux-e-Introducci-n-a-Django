import os

from django import get_version
from django.conf import settings
from django.shortcuts import render



def home(request):
    #Añadimos los ejemplos de instanciación con sus respectivas clases
    #Ejemplo de herencia múltiple
    class Estudiante(object): #< -------- definir clase padre 1
        def __init__(self, edad, nombre):
            self.edad = edad
            self.nombre = nombre
            
    class Instituto(object):  #<-----Padre 2
        def presentarInstituto(self):
            print("en EBAC")
            return "en EBAC"

    class Derecho(Estudiante, Instituto):#< --------- clase hija con herencia multiple
        def presentarse(self):
            print(f"Soy {self.nombre}, tengo {self.edad} años y estudio desarrollo Full Stack")
            return f"Soy {self.nombre}, tengo {self.edad} años y estudio desarrollo Full Stack"

    Jesús = Derecho(22, "Jesús Díaz")
  
    context = {
        "django_ver": Jesús.presentarse(),
        "python_ver": Jesús.presentarInstituto(),
    }

    return render(request, "pages/home.html", context)