from model_utils import Choices
from django.db import models

from wingtel.core.models import TimeStamped, SoftDeletable, CustomUser
from wingtel.subscriptions.models import Subscription


class Purchase(TimeStamped, SoftDeletable):
    """Represents a purchase for a user and their subscription(s)"""
    STATUS = Choices(
        ('pending', 'Pending'),
        ('overdue', 'Past Due'),
        ('complete', 'Complete'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    subscription = models.ForeignKey(Subscription, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS, default=STATUS.pending)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(null=True, db_index=True)
