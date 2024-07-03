from backend.entities.concrect.patient import Patient
from backend.entities.concrect.doctor import Doctor
from backend.entities.concrect.institution import Institution
from backend.entities.concrect.payment_method import PaymentMethod
from backend.entities.concrect.consultation_type import ConsultationType
from backend.entities.concrect.medical_appointment import MedicalAppointment

def to_medical_appointment(request):
    
    doctor = Doctor(id = request.POST.get('doctor'))
    patient = Patient(id = request.POST.get('patient'))
    institution = Institution(id = request.POST.get('institution'))
    paymentMethod = PaymentMethod(id = request.POST.get('paymentMethod'))
    consultationType = ConsultationType(id = request.POST.get('consultationType'))
    
    return MedicalAppointment(
        doctor = doctor,
        patient = patient,
        institution = institution,
        paymentMethod = paymentMethod,
        consultationType = consultationType,
        data = request.POST.get('data'),
        hour = request.POST.get('hour'),
        valuePay = request.POST.get('valuePay'),
        description = request.POST.get('description'),  
    )
    

def to_medical_appointment_model(request):
    medicalAppointment = to_medical_appointment(request)
    medicalAppointment.id = request.POST.get('model')
    return medicalAppointment