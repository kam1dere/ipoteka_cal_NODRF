from django.urls import path
from rest_framework import routers
from .views import MyView


# path('calculator/', include('calculator.urls')),
urlpatterns = [
    path('', MyView.as_view(), name='bank_list')
]