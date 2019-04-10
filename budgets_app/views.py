from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Budget, Transaction


class BudgetListView(LoginRequiredMixin, ListView):
    """

    """
    template_name = 'budgets/budget_list.html'
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Budget.objects.filter(
            user__username=self.request.user.user__username
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['budgets'] = Budget.objects.filter(
            budgets__user__username=self.request.user.username
            )
        return context


class TransactionListView(LoginRequiredMixin, ListView):
    """

    """
    template_name = 'budgets/transaction_list'
    context_object_name = 'transactions'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Transaction.objects.filter(
            user__username=self.request.user.user__username
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(
            transactions__user__username=self.request.user.username
            )
        return context
