from django.urls import path
from frontend import views
from frontend.controllers import institution, doctor, patient, laboratory_technician, province, municipality, permission, group, sickness

#routes views
urlpatterns = [
    # PAGES PUBLIC
    path('', views.index, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    
    # PAGES PRIVATE
    path('dashboard/', views.dashboard, name="dashboard"),
    
    path('permission/', permission.index, name="permission.index"),
    path('permission-group-plus/<int:id>', permission.group_plus, name="permission.group_plus"),
    path('permission-group-list/<int:id>', permission.group_list, name="permission.group_list"),  

    path('group/', group.index, name="group.index"),
    path('group/store', group.store, name="group.store"),
    path('group/update', group.update, name="group.update"),
    path('group/delete', group.delete, name="group.delete"),
    path('group-permission-plus/<int:id>', group.permission_plus, name="group.permission_plus"),
    path('group-permission-list/<int:id>', group.permission_list, name="group.permission_list"),    
    
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
    
    path('municipality/', municipality.index, name="municipality.index"),
    path('municipality/store', municipality.store, name="municipality.store"),
    path('municipality/update', municipality.update, name="municipality.update"),
    path('municipality/delete', municipality.delete, name="municipality.delete"), 
    
    path('institution/', institution.index, name="institution.index"),
    path('institution/store', institution.store, name="institution.store"),
    path('institution/update', institution.update, name="institution.update"),
    path('institution/delete', institution.delete, name="institution.delete"),          
    
    path('laboratory_technician/', laboratory_technician.index, name="laboratory_technician.index"),
    path('laboratory_technician/store', laboratory_technician.store, name="laboratory_technician.store"),
    path('laboratory_technician/update', laboratory_technician.update, name="laboratory_technician.update"),
    path('laboratory_technician/delete', laboratory_technician.delete, name="laboratory_technician.delete"),
    
    path('sickness/', sickness.index, name="sickness.index"),
    path('sickness/store', sickness.store, name="sickness.store"),
    path('sickness/update', sickness.update, name="sickness.update"),
    path('sickness/delete', sickness.delete, name="sickness.delete"),       
]

#route ajax (htmx)
urlpatterns += [
    
    path('hx-permission-plus/<int:id>/', group.plus, name="permission.plus"),
    path('hx-permission-list/<int:id>/', group.lists, name="permission.list"),
    
    path('hx-group-plus/<int:id>/', permission.plus, name="group.plus"),
    path('hx-group-list/<int:id>/', permission.lists, name="group.list"), 
            
    path('hx-municipality-province', municipality.province, name="municipality.getby-province"), 
]