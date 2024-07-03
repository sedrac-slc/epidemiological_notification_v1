from backend.entities.concrect.patient import Patient
from backend.entities.concrect.medical_appointment import MedicalAppointment

def to_medical_appointment(request):
    patient = Patient(id = request.POST.get('patient'))
    data = MedicalAppointment(accomplished = request.POST.get('accomplished'), description = request.POST.get('description'),  patient = patient)
    return data

def to_medical_appointment_model(request):
    patient = Patient(id = request.POST.get('patient'))
    data = MedicalAppointment(id = request.POST.get('model') , accomplished = request.POST.get('accomplished'), description = request.POST.get('description'), patient = patient)
    return data