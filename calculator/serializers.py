from rest_framework import serializers
from .models import Bank


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = '__all__'
            # ['name', 'term_min', 'term_max',
            #        'rate_min', 'rate_max', 'payment_min',
            #        'payment_max']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['deposit'] = self.context['deposit']
        representation['first_payment'] = self.context['first_payment']
        representation['term'] = self.context['term']
       # representation['payment_monthly'] = self.context['payment_monthly']
        return representation
