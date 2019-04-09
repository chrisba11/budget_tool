from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone


class Budget(models.Model):
    """

    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='budgets',
        )

    name = models.CharField(
        max_length=255,
        default='That Which Shall Not Be Named',
        )

    total_budget = models.FloatField(
        default=0
    )

    remaining_budget = models.FloatField(

    )

    @property
    def balance(self):
        self.transactions

    def __repr__(self):
        return '<Budget: {} @ {}>'.format(self.name, self.id)

    def __str__(self):
        return '{} @ {}'.format(self.name, self.id)


class Transactions(models.Model):
    """

    """
    OPTIONS = (
        ('+', 'Withdrawal'),
        ('-', 'Deposit'),
    )

    budget = models.ForeignKey(
        Budget,
        on_delete=models.CASCADE,
        related_name='transactions',
        null=False
    )

    trans_type = models.CharField(
        max_length=16,
        choices=OPTIONS,
        default='Withdrawal',
    )

    amount = models.FloatField(
        max_length=255,
        null=False,
    )

    description = models.CharField(
        max_length=255,
        default='No Description Provided',
    )

    def __repr__(self):
        return '<Transaction: {} of {}>'.format(
            self.trans_type,
            self.amount,
            )

    def __str__(self):
        return '{}  {}'.format(
            self.trans_type,
            self.amount,
            )
