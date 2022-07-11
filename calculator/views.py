from django.utils.datastructures import MultiValueDictKeyError

from .models import Bank
from django.views.generic import ListView
from .math import monthly_payment


class MyView(ListView):
    model = Bank
    template_name = 'bank_list.html'
    context_object_name = 'reqs'

    def get_queryset(self):
        queryset = Bank.objects.all().order_by('rate_min')
        request = self.request.GET
        try:
            deposit = int(request['deposit'])
            first_payment = int(request['first_payment'])
            term_fk = int(request['term_fk'])
            queryset = queryset.annotate(fact_pay=monthly_payment(deposit, first_payment, term_fk, stavka='rate_min'))
            return queryset
        except MultiValueDictKeyError:
            print('Введены неверные данные')
            return queryset


"""
Нормальный вывод
сделать проверку введеных полей
вывод в зависимости от общей суммы кредита (могут бить потолки)
Сделать нормальную фильтрацию
нулевой ввод
"""
