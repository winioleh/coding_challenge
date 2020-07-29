from rest_framework import viewsets

from wingtel.core.models import TelecommunicationCompany, CustomUser
from wingtel.core.serialisers import TCSerializer, CustomUserSerializer
# Create your views here.


class TCViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing telecommunication companies.
    """
    queryset = TelecommunicationCompany.objects.all()
    serializer_class = TCSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing telecommunication companies.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
