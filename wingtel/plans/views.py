from rest_framework import viewsets

from wingtel.plans.models import Plan
from wingtel.plans.serializers import PlanSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class PlanViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
