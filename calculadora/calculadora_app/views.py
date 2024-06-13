from django.shortcuts import render
from django.http import HttpResponse

def Procedimiento(request):
    resultado = None
    
    if request.method == 'POST':
        xi = request.POST.get('xi_valores', '')  # Obtener el valor de xi_valores del formulario
        fi = request.POST.get('fi_valores', '')  # Obtener el valor de fi_valores del formulario
        
        # Validar y convertir los datos a enteros (puedes manejar excepciones aquí si no son números válidos)
        try:
            xi = int(xi)
            fi = int(fi)
            resultado = xi + fi  # Realizar la operación de suma
        except ValueError:
            resultado = "Error: Por favor ingrese números válidos"

    return render(request, 'index.html', {'resultado': resultado})
