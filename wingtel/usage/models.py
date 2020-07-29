from django.db import models
from model_utils import Choices
from datetime import date

from wingtel.subscriptions.models import Subscription


class UsageRecord(models.Model):
    """Raw usage record for a subscription"""
    subscription = models.ForeignKey(Subscription, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    usage_date = models.DateField(default=date.today())
    TYPE = Choices(
        ('data', 'Data'),
        ('voice', 'Voice'),

    )
    usage_type = models.CharField(max_length=10, choices=TYPE, default=TYPE.data)
    resource_used = models.IntegerField(null=True)
