from rest_framework import serializers
from .models import Transaction
from accounts.models import Account
from categories.models import Category

class TransactionSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), allow_null=True)

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'category', 'amount', 'description', 'date', 'transaction_type', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        user = self.context['request'].user
        if data['account'].user != user:
            raise serializers.ValidationError("You can't create transaction for another user's account")
        if data['category'].user != user:
            raise serializers.ValidationError("You can't create transaction for another user's category")
        if data['category'] and data['category'].category_type != data['transaction_type']:
            raise serializers.ValidationError("Category type must match transaction type.")
        return data