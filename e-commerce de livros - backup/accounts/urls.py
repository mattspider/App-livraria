from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.user_login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('cadastro/',views.adc_conta, name='cadastro')
]