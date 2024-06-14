from django.shortcuts import render
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from .models import *
from django.http import HttpResponse
import math

def Dif_Divididas(request):
    pol_nomio= ''
    polinomio_simplificado = ''
    tabla_final = []
    title = ''
    
    #Importante
    objeto = tbl_Ecuaciones()

    if request.method == 'POST':
        xi_str_inp = request.POST.get('xi_valores','')
        fi_str_inp = request.POST.get('fi_valores','')

        # INGRESO , Datos de prueba
        xi = [float(x.strip()) for x in xi_str_inp.replace(' ', '').split(',') if x.strip()]
        fi = [float(x.strip()) for x in fi_str_inp.replace(' ', '').split(',') if x.strip()]
        

        # PROCEDIMIENTO

        # Tabla de Diferencias Divididas Avanzadas
        titulo = ['i   ','xi  ','fi  ']
        n = len(xi)
        ki = np.arange(0,n,1)
        tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
        tabla = np.transpose(tabla)

        # diferencias divididas vacia
        dfinita = np.zeros(shape=(n,n),dtype=float)
        tabla = np.concatenate((tabla,dfinita), axis=1)

        # Calcula tabla, inicia en columna 3
        [n,m] = np.shape(tabla)
        diagonal = n-1
        j = 3
        while (j < m):
            # Añade título para cada columna
            titulo.append('F['+str(j-2)+']')

            # cada fila de columna
            i = 0
            paso = j-2 # inicia en 1
            while (i < diagonal):
                denominador = (xi[i+paso]-xi[i])
                numerador = tabla[i+1,j-1]-tabla[i,j-1]
                tabla[i,j] = numerador/denominador
                i = i+1
            diagonal = diagonal - 1
            j = j+1

        # POLINOMIO con diferencias Divididas
        # caso: puntos equidistantes en eje x
        dDividida = tabla[0,3:]
        n = len(dfinita)

        # expresión del polinomio con Sympy
        x = sp.Symbol('x')
        polinomio = fi[0]
        for j in range(1,n,1):
            factor = dDividida[j-1]
            termino = 1
            for k in range(0,j,1):
                termino = termino*(x-xi[k])
            polinomio = polinomio + termino*factor

        # simplifica multiplicando entre (x-xi)
        polisimple = polinomio.expand()

        # polinomio para evaluacion numérica

        px = sp.lambdify(x,polisimple)

        # Puntos para la gráfica
        muestras = 101
        a = np.min(xi)
        b = np.max(xi)
        pxi = np.linspace(a,b,muestras)
        pfi = px(pxi)

        #Salida de las ecuaciones
        tabla_final = tabla.tolist()
        
        pol_nomio = polinomio
        
        title = titulo
        
        polinomio_simplificado = polisimple
        
        #Guardar en la DataBase
        objeto.xi_ecuacion = xi
        objeto.fi_ecuacion = fi
        objeto.ecuacion = polinomio
        objeto.ecuacion_simplificada = polisimple

    return render(request, 'index.html', {'polinomio':pol_nomio, 'simplificado':polinomio_simplificado
                                          , 'tabla':tabla_final, 'titulos':title})


def funcion(x, y, ecuacion):
    expr = sp.sympify(ecuacion)
    return expr.subs({sp.symbols('x'): x, sp.symbols('y'): y})

def Euler_Method(request):
    resultados = []
    if request.method == 'POST':
        h = float(request.POST.get('h'))
        s = float(request.POST.get('s'))
        ecuacion = request.POST.get('ecuacion')

        x, y = sp.symbols('x y')

        n = int((s / h) + 1)
        x_vals = np.zeros(n)
        y_vals = np.zeros(n)
       

        for i in range(1, n):
            y_vals[i] = y_vals[i - 1] + funcion(x_vals[i - 1], y_vals[i - 1], ecuacion) * h
            x_vals[i] = x_vals[i - 1] + h
            resultados.append((x_vals[i], y_vals[i]))
        
    return render(request, 'euler.html', {'resultados':resultados})