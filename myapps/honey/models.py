from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, Case, When, DecimalField, F
from decimal import Decimal

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
    
    
    #Corregir esto
    
    def save(self, *args, **kwargs):
        if self.category  in  [self.CategoryChoices.EXPENSE, self.CategoryChoices.LEND]:
            self.amount = -abs(self.amount)  # Ensure amount is negative
            
        elif self.category in[self.CategoryChoices.INCOME, self.CategoryChoices.BORROW]:
            if self.amount < 0:
                raise ValueError("Amount for income or borrowing must be positive.")
            self.amount = abs(self.amount)
        
        super().save(*args, **kwargs)
    
    def get_balance(self):
        balance = Transaction.objects.filter(user=self.user).aggregate(
            total=Sum(
                Case(
                    When(category=self.CategoryChoices.INCOME, then=F('amount')),
                    When(category=self.CategoryChoices.EXPENSE, then=-F('amount')),
                    default=0,
                    output_field=DecimalField()
                )
            )
        )['total'] or 0
        return balance

    def __str__(self):
        return f"Transaction of {self.amount} at {self.timestamp} )"
        

    
