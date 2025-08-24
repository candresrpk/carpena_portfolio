from django.urls import path
from . import views

app_name = 'honey'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.users_dashboard, name='users_dashboard'),
    path('test/dashboard/', views.non_users_dashboard, name='non_users_dashboard'),
    path('create_transaction/', views.create_user_transaction, name='create_user_transaction'),
]