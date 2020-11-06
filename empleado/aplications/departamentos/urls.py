
from django.contrib import admin
from django.urls import path

from.import views
urlpatterns = [
    path('prueba1/', views.Prueba1View.as_view()),
]
