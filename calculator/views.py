from .models import Bank
from django.views.generic import ListView


class MyView(ListView):
    model = Bank
    template_name = 'bank_list.html'
    context_object_name = 'reqs'

    def get_queryset(self):
        nam = self.request.GET['message']
        queryset = Bank.objects.get(id=nam)
        return queryset






