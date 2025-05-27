from django.urls import path
from . import views

app_name = 'dreams'

urlpatterns = [
    path('', views.dream_input, name='dream_input'),  # Ana sayfa yönlendirmesi
    path('dreams/', views.dream_list, name='dream_list'),  # Rüya listeleme sayfası,
    path('generate/', views.generate_interpretation, name='generate_interpretation'),


]
