from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from backend.service.concrect.consultation_type import ConsultationTypeService
from backend.dto.consultation_type import to_consultation_type, to_consultation_type_model

consultationTypeService = ConsultationTypeService()

# Create your views here.
def index(request):
    data = consultationTypeService.findAllPage(request)
    return render(request, "pages/consultation-type.html", {
        'data': data, 
        'title': 'Tipo de consulta',
        'store': reverse('consultation_type.store'),
        'update': reverse('consultation_type.update'),
        'delete': reverse('consultation_type.delete') 
    })

def store(request):
    if request.method != "POST": return redirect('consultation_type.index')
    consultationTypeService.save(to_consultation_type(request))
    messages.success(request, 'Tipo de consulta cadastrada com successo!')
    return redirect('consultation_type.index')
   

def update(request):
    if request.method != "POST": return redirect('consultation_type.index') 
    consultationTypeService.update(to_consultation_type_model(request))
    messages.success(request, 'Tipo de consulta editada com successo!')
    return redirect('consultation_type.index')

def delete(request):
    if request.method != "POST": return redirect('consultation_type.index')
    consultationTypeService.hidden(request.POST.get('model'))
    messages.success(request, 'Tipo de consulta eliminada com successo!')
    return redirect('consultation_type.index')