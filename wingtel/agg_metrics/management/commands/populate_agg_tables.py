from datetime import date

from django.core.management.base import BaseCommand
from wingtel.agg_metrics.models import AggUsageRecordsDay
from django.db.models import Sum
from faker import Factory
from wingtel.usage.models import UsageRecord

faker = Factory.create()


class Command(BaseCommand):
    help = 'Populate fdsds usage models with data from the raw usage models'

    def handle(self, *args, **options):
        dates_and_type = list(set(UsageRecord.objects.filter(
            usage_date__lt=date.today()
        ).values_list('usage_date', 'usage_type')))
        import logging
        logg = logging.getLogger(__name__)
        logg.warning('@@@@@@@@@@@@@@')
        logg.warning(dates_and_type)
        logg.warning(len(dates_and_type))
        usage_records = []
        for _date, usage_type in dates_and_type:
            usage_records.append(list(UsageRecord.objects.filter(usage_date=_date, usage_type=usage_type)))
        logg.warning(len(usage_records))

        total_prices = UsageRecord.objects.values('usage_date', 'usage_type').filter(usage_date__lt=date.today())\
            .annotate(total_price=Sum('price')).values_list('total_price', flat=True)
        resources_used = UsageRecord.objects.values('usage_date', 'usage_type').filter(
            usage_date__lt=date.today()
        ).values(
            'usage_date',
            'usage_type'
        ).annotate(total_used=Sum('resource_used')).values_list('total_used', flat=True)
        logg.warning(len(resources_used))
        logg.warning(len(total_prices))

        agg_records = []
        for usage_record, resource_used, total_price, _date in zip(usage_records, resources_used, total_prices, dates_and_type):
            agg_records.append(
                AggUsageRecordsDay(
                    total_price=total_price,
                    resource_used=resource_used,
                    usage_date=_date[0],
                    usage_type=_date[1])
            )
            logg.warning('@@@@@@DATE@@@@@@@@')
            logg.warning(_date[0])
        agg_records = AggUsageRecordsDay.objects.bulk_create(agg_records)
        for agg_record, usage_record in zip(agg_records, usage_records):
            agg_record.usage_records.set(usage_record)
            agg_record.save()