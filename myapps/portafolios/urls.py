from django.urls import path
from . import views

app_name = 'portafolios'

urlpatterns = [
    path('', views.home, name='home'),
    path('projectsList/', views.projectsList, name='projectsList'),
    path('create_project/', views.create_project, name='create_project'),
    path('faq/', views.faq, name='faq'),
]