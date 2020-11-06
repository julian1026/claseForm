from django.contrib import admin
from django.urls import path

from.import views
app_name="home_app"
urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('lista/', views.PruebaListView.as_view()),
    path('listarUsuario/', views.ListarPruebatListView.as_view()),
    path('add/', views.PruebaCreateView.as_view()),
    path('update/<pk>/', views.PruebaUpdate.as_view()),
]

