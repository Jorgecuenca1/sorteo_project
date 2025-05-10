from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Rifa, Posicion

def index(request):
    rifas = Rifa.objects.all()
    return render(request, 'rifas/index.html', {'rifas': rifas})

def rifa_detalle(request, rifa_id):
    rifa = get_object_or_404(Rifa, pk=rifa_id)
    posiciones = rifa.posiciones.order_by('numero')
    return render(request, 'rifas/rifa.html', {'rifa': rifa, 'posiciones': posiciones})

@csrf_exempt
def reservar_posicion(request, posicion_id):
    if request.method == 'POST':
        pos = get_object_or_404(Posicion, pk=posicion_id)

        if pos.reservado:
            return JsonResponse({'status': 'fail', 'message': 'Esta posición ya fue reservada.'})

        pos.nombre_completo = request.POST.get('nombre')
        pos.correo = request.POST.get('correo')
        pos.celular = request.POST.get('celular')
        pos.comprobante = request.FILES.get('comprobante')
        pos.reservado = True
        pos.save()

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail', 'message': 'Método no permitido'})
