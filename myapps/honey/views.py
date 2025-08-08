from django.shortcuts import render
from .models import Transaction, Balance
# Create your views here.



def home(request):
    return render(request, 'honey/home.html')

def users_dashboard(request):
    
    # transactions = Transaction.objects.filter(user=request.user).order_by('-timestamp')
    # balance = Balance.objects.get(user=request.user)
    
    # context = {
    #     'transactions': transactions,
    #     'balance': balance,
    # }
    
    return render(request, 'honey/users_dashboard.html')

def non_users_dashboard(request):
    return render(request, 'honey/non_users_dashboard.html')
