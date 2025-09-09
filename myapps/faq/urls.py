from django.urls import path
from . import views

app_name = 'faq'


urlpatterns = [
    path('', views.home, name='home'),
    path('question/<int:pk>/', views.Question_detail, name='detail'),
]