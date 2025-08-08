from django.contrib import admin
from .models import Transaction
# Register your models here.


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'description', 'timestamp')
    list_filter = ('category', 'timestamp', 'user')
    search_fields = ('description', 'user__username', 'user__email')
    ordering = ('-timestamp',)
