from credits.models import Transaction,Payment
from rest_framework.serializers import ModelSerializer

class TransactionSerializer(ModelSerializer):
    class Meta:
        model=Transaction
        fields='__all__'

class PaymentSerializer(ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'
