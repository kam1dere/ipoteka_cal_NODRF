from django.urls import path, include
from rest_framework import routers
from .views import BankList, BankViewSet

# path('calculator/', include('calculator.urls')),
router = routers.SimpleRouter()
router.register(r'api', BankViewSet)
urlpatterns = [
    path('', BankList.as_view(), name='bank_list')
]

urlpatterns += router.urls
