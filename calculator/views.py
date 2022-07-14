from django.db.models import PositiveIntegerField, ExpressionWrapper, Q
from django.utils.datastructures import MultiValueDictKeyError

from .models import Bank
from django.views.generic import ListView
from .math import monthly_payment


class MyView(ListView):
    model = Bank
    template_name = 'bank_list.html'
    context_object_name = 'banks'

    def get_queryset(self):
        queryset = Bank.objects.all().order_by('rate_min')
        request = self.request.GET
        try:
            deposit = int(request['deposit'])
            first_payment = int(request['first_payment'])
            term = int(request['term'])
            summa = deposit - first_payment
            queryset = Bank.objects.filter(Q(payment_min__lte=summa) & Q(payment_max__gte=summa) &
                                           Q(term_min__lte=term) & Q(term_max__gte=term)).order_by('rate_min')
            queryset = queryset.annotate(fact_pay=ExpressionWrapper(monthly_payment(summa, term, stavka='rate_min'),
                                                                    output_field=PositiveIntegerField()))
            return queryset
        except MultiValueDictKeyError:
            print('Введены неверные данные')
            return queryset
        except ValueError:
            print('Введены неверные данные')
            return queryset


