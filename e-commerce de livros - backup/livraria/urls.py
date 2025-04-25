from django.urls import path
from . import views


urlpatterns= [
    path('', views.index, name='home'),
    path('index/',views.index,name='index'),
    path('produto/<int:id>',views.produto,name='produto'),
    path('carrinho/',views.carrinho,name='carrinho'),
    path('delete/<int:id>',views.deletar,name='deletar'),
    path('checkout/',views.checkout,name='checkout')
]