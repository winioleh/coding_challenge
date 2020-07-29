from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import F

from wingtel.usage.models import UsageRecord
from wingtel.usage.serialisers import UsageRecordSerializer
# Create your views here.


class UsageRecordViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing subscription.
    """
    queryset = UsageRecord.objects.all()
    serializer_class = UsageRecordSerializer


@api_view(['GET'])
def get_subscriptions_with_exceeded_price_limit(request):
    price_limit = request.GET.get('price_limit')
    qs = UsageRecord.objects.values('subscription__id').filter(
        price__gt=price_limit
    ).annotate(
        limit_exceeded_on=F('price') - price_limit
    ).values(
        'limit_exceeded_on',
        'usage_type',
        'subscription__id'
    )
    return Response(qs)
