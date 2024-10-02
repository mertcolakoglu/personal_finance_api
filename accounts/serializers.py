from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'account_type', 'balance', 'currency', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']