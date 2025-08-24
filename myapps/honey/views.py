from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transaction
# Create your views here.



def home(request):
    return render(request, 'honey/home.html')

def users_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    
    
    transactions = Transaction.objects.filter(user=request.user).order_by('-timestamp')
    
    income = transactions.filter(category= Transaction.CategoryChoices.INCOME)
    expenses = transactions.filter(category= Transaction.CategoryChoices.EXPENSE)
    borrow = transactions.filter(category= Transaction.CategoryChoices.BORROW)
    lend = transactions.filter(category=Transaction.CategoryChoices.LEND)
    
    
    create_user_transaction = TransactionForm()
    context = {
        'transactions': transactions,
        'income': income,
        'expenses': expenses,
        'borrow': borrow,
        'lend': lend,
        'create_user_transaction': create_user_transaction,
    }
    
    return render(request, 'honey/users_dashboard.html', context)


def non_users_dashboard(request):
    return render(request, 'honey/non_users_dashboard.html')


def create_user_transaction(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('honey:users_dashboard')
    else:
        form = TransactionForm()
    return redirect('honey:users_dashboard')