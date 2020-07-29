from django.db import models
from model_utils import Choices

from wingtel.plans.models import Plan
from wingtel.core.models import TimeStamped, SoftDeletable, TelecommunicationCompany, CustomUser


class Subscription(TimeStamped, SoftDeletable):
    """Represents a subscription with Sprint for a user and a single device"""
    STATUS = Choices(
        ('new', 'New'),
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('expired', 'Expired'),
    )
    # Owning user
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, null=True, on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=STATUS, default=STATUS.new)
    device_id = models.CharField(max_length=20, default='')
    phone_number = models.CharField(max_length=20, default='')
    phone_model = models.CharField(max_length=128, default='')
    provider_company = models.ForeignKey(TelecommunicationCompany, on_delete=models.PROTECT)
    effective_date = models.DateTimeField(null=True)

