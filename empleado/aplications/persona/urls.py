from django.contrib import admin
from django.urls import path

from.import views
urlpatterns = [
    path('prueba2/', views.Prueba2View.as_view()),
]
