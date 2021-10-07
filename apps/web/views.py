from django.shortcuts import render, redirect

from .models import *
# Create your views here.



def index(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        salario = request.POST.get('salario')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        print("su nombre es " + nombre)

        model_empleado = empleado(name=nombre,
                                lastname=apellido,
                                Salary=salario,
                                telefono=telefono,
                                direcciono=direccion)

        model_empleado.save()
        return redirect('webexa:index')

    elif request.method == "GET":
        return render(request, 'index.html')
