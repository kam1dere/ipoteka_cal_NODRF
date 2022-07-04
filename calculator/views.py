from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Bank
from .serializers import BankSerializer


class BankFilter(filters.FilterSet):
    class Meta:
        model = Bank
        fields = ['term_min', 'rate_min', 'payment_min']


class BankList(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BankFilter
