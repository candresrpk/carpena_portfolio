from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Transaction(models.Model):
    
    class CategoryChoices(models.TextChoices):
        INCOME = 'IN', 'Income'
        EXPENSE = 'EX', 'Expense'
        BORROW = 'BR', 'Borrow'
        LEND = 'LE', 'Lend'
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CategoryChoices.choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Transaction of {self.amount} at {self.timestamp} - ({self.get_kind_display()})"
    
class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_expense = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_borrowed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_lent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Balance for {self.user.username} - Net: {self.net_balance}"
    
    @property
    def net_balance(self):
        return self.total_income - self.total_expense + self.total_lent - self.total_borrowed        
     
    
