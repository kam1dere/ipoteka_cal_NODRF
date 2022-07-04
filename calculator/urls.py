from django.urls import path, include
from rest_framework import routers
from .views import BankList


# path('calculator/', include('calculator.urls')),
urlpatterns = [
    path('', BankList.as_view(), name='redir')
]
