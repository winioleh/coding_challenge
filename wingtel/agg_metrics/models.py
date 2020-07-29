from django.db import models
from wingtel.usage.models import UsageRecord
from model_utils import Choices

# Create your models here.


class AggUsageRecordsDay(models.Model):
    usage_date = models.DateField(null=False)
    total_price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    resource_used = models.IntegerField(null=False)
    usage_records = models.ManyToManyField(UsageRecord)
    TYPE = Choices(
        ('data', 'Data'),
        ('voice', 'Voice'),

    )
    usage_type = models.CharField(max_length=10, choices=TYPE, default=TYPE.data)
