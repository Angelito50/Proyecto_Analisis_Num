from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Create your views here.
def Procedimiento(request):
    documento = ''
    #if request.method=="POST":
        #if "mandar-dato" in request.POST:
            
    # Polinomio interpolación
    # Diferencias Divididas de Newton
    # Tarea: Verificar tamaño de vectores,
    # verificar puntos equidistantes en x
    xi_str = request.POST.get('xi', '')
    fi_str = request.POST.get('fi', '')

    # INGRESO , Datos de prueba
    # Convertir las cadenas de entrada en arrays de numpy
    #xi = np.array([float(x) for x in xi_str.split(',') if x.strip()])
    #fi = np.array([float(f) for f in fi_str.split(',') if f.strip()])

    xi = np.array([5,11,17,20])
    fi = np.array([8,15,21,25])

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

    # SALIDA
    np.set_printoptions(precision = 4)
    """
    print('Tabla Diferencia Dividida')
    print([titulo])
    print(tabla)
    """
    print('dDividida: ')
    print(dDividida)
    print('polinomio: ')
    print(polinomio)
    print('polinomio simplificado: ' )
    print(polisimple)

    """
    # Gráfica
    plt.plot(xi,fi,'o', label = 'Puntos')
    ##for i in range(0,n,1):
    ##    plt.axvline(xi[i],ls='--', color='yellow')
    plt.plot(pxi,pfi, label = 'Polinomio')
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Diferencias Divididas - Newton')
    plt.show()
    """
    
    plantillaExterna = open("C:/Users/Angel/Desktop/PROYECTO_ANS/calculadora/calculadora_app/template/index.html")
    templ = Template(plantillaExterna.read())
    plantillaExterna.close()
    
    #Variables retornan valores
    dDivid = dDividida
    pol = polinomio 
    pol_simpl = polisimple
    
    contexto = Context({'dDivid':dDivid, 'pol':pol, 'pol_simpl':pol_simpl})
    documento = templ.render(contexto)
    #documento = render(request, 'index.html', contexto)
    return HttpResponse(documento)
    #return documento