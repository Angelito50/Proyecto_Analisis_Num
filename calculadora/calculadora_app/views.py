from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import *
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def Procedimiento(request):
    xi = tbl_Ecuaciones()
    fi = tbl_Ecuaciones()
    
    if request.method == 'POST':
        # Obtener los datos del formulario POST y guardar en la base de datos
        
        xi.xi_ecuacion = request.POST['xi_valores']
        xi.save()
        
        fi.fi_ecuacion = request.POST['fi_valores']
        fi.save()
        
        return HttpResponse("Guardado correctamente")

    return render(request, 'index.html', {'xi_ecuacion': xi.xi_ecuacion, 'fi_ecuacion': fi.fi_ecuacion})