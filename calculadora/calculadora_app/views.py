from django.shortcuts import render
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from django.http import HttpResponse

def Procedimiento(request):
    pol_nomio= ''
    polinomio_simplificado = ''
    
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
        x = sym.Symbol('x')
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
        px = sym.lambdify(x,polisimple)

        # Puntos para la gráfica
        muestras = 101
        a = np.min(xi)
        b = np.max(xi)
        pxi = np.linspace(a,b,muestras)
        pfi = px(pxi)

        #Salida de las ecuaciones
        
        
        pol_nomio = polinomio
        
        
        polinomio_simplificado = polisimple

    return render(request, 'index.html', {'polinomio':pol_nomio, 'simplificado':polinomio_simplificado})