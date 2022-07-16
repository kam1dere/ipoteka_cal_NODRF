from rest_framework import serializers
from .models import Bank


# Для ListApi
class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['deposit'] = self.context['deposit']
        representation['first_payment'] = self.context['first_payment']
        representation['term'] = self.context['term']
        representation['payment_monthly'] = instance.fact_pay
        return representation


# Для ViewSet
class BankSerializerAPI(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = '__all__'
