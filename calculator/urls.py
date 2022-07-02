from django.urls import path, include
from rest_framework import routers
from .views import my_view


# path('calculator/', include('calculator.urls')),
urlpatterns = [
    path('', my_view, name='redir')
]
