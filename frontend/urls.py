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
    path('patient/', patient.index, name="patient.index"),   
    path('province/', province.index, name="province.index"),
    path('municipal/', municipal.index, name="municipal.index"),
    path('permission/', permission.index, name="permission.index"),
    path('institution/', institution.index, name="institution.index"),
    path('laboratory_technician/', laboratory_technician.index, name="laboratory_technician.index"),
]