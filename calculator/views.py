from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Bank
from .serializers import BankSerializer
from django.shortcuts import render
from django.views.generic.list import ListView


class BankFilter(filters.FilterSet):
    class Meta:
        model = Bank
        fields = {
            'term_min': ['gte'],
            'rate_min': ['gte'],
            'payment_min': ['gte'],

        }


class BankList(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BankFilter
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'bank': self.object}, template_name='redir.html')



