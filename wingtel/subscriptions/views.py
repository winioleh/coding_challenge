from rest_framework import viewsets


from wingtel.subscriptions.models import Subscription
from wingtel.subscriptions.serialisers import SubscriptionSerializer
# Create your views here.


class SubscriptionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing subscription.
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
