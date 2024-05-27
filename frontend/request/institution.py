from django.shortcuts import render
from backend.service.concrect.institution import InstitutionService

# Create your views here.
def index(request):
    service = InstitutionService()
    data = service.findAllPage(request)
    return render(request, "pages/institution.html", { 'title': 'Instituição', 'data': data})