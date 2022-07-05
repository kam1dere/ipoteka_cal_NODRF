from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import generics, viewsets
from django_filters import rest_framework as filters
from .models import Bank
from .serializers import BankSerializer


class BankFilter(filters.FilterSet):
    class Meta:
        model = Bank
        fields = {
            'term_min': ['gte'],
            'rate_min': ['gte'],
            'payment_min': ['gte'],

        }


class BankList(generics.ListAPIView):
    # queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BankFilter
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        # self.object = self.get_object()
        queryset = Bank.objects.all()
        return Response({'banks': queryset}, template_name='calculator.html')


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer



