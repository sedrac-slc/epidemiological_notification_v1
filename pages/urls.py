
from django.urls import path
from .enum.link import LinkEnum
from . import views

urlpatterns = [
    path('', views.index, name = LinkEnum.HOME.name ),
    path('login/', views.login, name = LinkEnum.LOGIN.name ),
    path('register/', views.login, name = LinkEnum.REGISTER.name ),
]