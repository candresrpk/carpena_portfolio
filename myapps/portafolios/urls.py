from django.urls import path
from . import views

app_name = 'portafolios'

urlpatterns = [
    path('', views.home, name='home'),
    path('projectsList/', views.projectsList, name='projectsList'),
]