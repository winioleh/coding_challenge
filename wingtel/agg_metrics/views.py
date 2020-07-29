from datetime import datetime

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from wingtel.agg_metrics.models import AggUsageRecordsDay
from wingtel.usage.models import UsageRecord
from wingtel.agg_metrics.serializers import AggUsageRecordsDaySerializer


# Create your views here.


class AggUsageViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing telecommunication companies.
    """
    queryset = AggUsageRecordsDay.objects.all()
    serializer_class = AggUsageRecordsDaySerializer


@api_view(['GET'])
def usage_metrics(request):
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    usage_type = request.GET.get('usage_type')
    filters = {}
    if date_to:
        filters['usage_date__lte'] = datetime.strptime(date_to, '%Y-%m-%d')
    if date_from:
        filters['usage_date__gt'] = datetime.strptime(date_from, '%Y-%m-%d')
    if usage_type:
        filters['usage_type'] = usage_type
    agg_records = AggUsageRecordsDay.objects.filter(**filters).values(
        'usage_date', 'total_price', 'resource_used','usage_records'
    )
    res = []
    total_usage = 0
    for agg_record in agg_records:

        usage_records_ids = agg_record['usage_records']
        if isinstance(usage_records_ids, int):
            usage_records_ids = [usage_records_ids]
        subscription__ids = UsageRecord.objects.filter(id__in=usage_records_ids).values_list('subscription__id', flat=True)
        tmp_record = {
            'subscription__ids': subscription__ids,
            'total_price': agg_record['total_price']
        }
        res.append(tmp_record)
        total_usage += agg_record['resource_used']
    result = {
        "data": res,
        "date_range_total_usage": {
            "date_from": date_from,
            "date_to": date_to,
            "total_usage": total_usage
        }
    }
    return Response(result)
