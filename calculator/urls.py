from django.urls import path, include
from rest_framework import routers
from .views import BankList, BankViewSet


# path('calculator/', include('calculator.urls')),
router = routers.SimpleRouter()
router.register(r'api', BankViewSet)
urlpatterns = [
    path('<int:pk>/', BankList.as_view(), name='calculator')
]

urlpatterns += router.urls
