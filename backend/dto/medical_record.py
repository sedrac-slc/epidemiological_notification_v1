from backend.entities.concrect.sickness import Sickness
from backend.entities.concrect.medical_record import MedicalRecord

def to_medical_record(request):
    sickness = Sickness(id = request.POST.get('sickness'))
    data = MedicalRecord(name = request.POST.get('name'),  sickness = sickness)
    return data

def to_medical_record_model(request):
    sickness = Sickness(id = request.POST.get('sickness'))
    data = MedicalRecord(id = request.POST.get('model') , name = request.POST.get('name'), sickness = sickness)
    return data