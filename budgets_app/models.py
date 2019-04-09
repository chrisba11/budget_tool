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

    remaining_balance = models.FloatField(
        
    )

# Create your models here.
