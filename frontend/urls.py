from django.urls import path
from frontend import views
from frontend.controllers import institution, doctor, patient, laboratory_technician, province, municipal, permission, role

urlpatterns = [
    # PAGES PUBLIC
    path('', views.index, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    
    # PAGES PRIVATE
    path('dashboard/', views.dashboard, name="dashboard"),

    path('role/', role.index, name="role.index"),
    
    path('doctor/', doctor.index, name="doctor.index"),
    path('doctor/store', doctor.store, name="doctor.store"),
    path('doctor/update', doctor.update, name="doctor.update"),
    path('doctor/delete', doctor.delete, name="doctor.delete"),    
    
    path('patient/', patient.index, name="patient.index"),
    path('patient/store', patient.store, name="patient.store"),
    path('patient/update', patient.update, name="patient.update"),
    path('patient/delete', patient.delete, name="patient.delete"),        
     
    path('province/', province.index, name="province.index"),
    path('province/store', province.store, name="province.store"),
    path('province/update', province.update, name="province.update"),
    path('province/delete', province.delete, name="province.delete"),
    
    path('municipal/', municipal.index, name="municipal.index"),
    path('municipal/store', municipal.store, name="municipal.store"),
    path('municipal/update', municipal.update, name="municipal.update"),
    path('municipal/delete', municipal.delete, name="municipal.delete"), 
    path('hx-municipal-province', municipal.province, name="municipal.getby-province"), 
    
    path('permission/', permission.index, name="permission.index"),
    
    path('institution/', institution.index, name="institution.index"),
    path('institution/store', institution.store, name="institution.store"),
    path('institution/update', institution.update, name="institution.update"),
    path('institution/delete', institution.delete, name="institution.delete"),          
    
    path('laboratory_technician/', laboratory_technician.index, name="laboratory_technician.index"),
    path('laboratory_technician/store', laboratory_technician.store, name="laboratory_technician.store"),
    path('laboratory_technician/update', laboratory_technician.update, name="laboratory_technician.update"),
    path('laboratory_technician/delete', laboratory_technician.delete, name="laboratory_technician.delete"),       
]