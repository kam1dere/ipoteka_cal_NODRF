from django.urls import path, include
from rest_framework import routers
from .views import BankList, BankViewSet, BankApiList

# path('calculator/', include('calculator.urls')),
router = routers.SimpleRouter()
router.register(r'api', BankViewSet)
urlpatterns = [
    path('', BankList.as_view(), name='bank_list'),
    path('DRFList', BankApiList.as_view(), name='bank_list_drf')
]

urlpatterns += router.urls
