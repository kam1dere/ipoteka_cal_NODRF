from django.urls import path, include
from rest_framework import routers
from .views import BankList


# path('calculator/', include('calculator.urls')),
urlpatterns = [
    path('<int:pk>/', BankList.as_view(), name='redir')
]
