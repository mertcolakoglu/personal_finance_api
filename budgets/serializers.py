from rest_framework import serializers
from .models import Budget
from categories.models import Category


class BudgetSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Budget
        fields = ['id', 'category', 'amount', 'period', 'start_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        user = self.context['request'].user
        if data['category'].user != user:
            raise serializers.ValidationError('You can only create budgets for your own categories.')
        if data['category'].category_type == 'expense':
            raise serializers.ValidationError('Budgets can only be created for expense categories.')
        return data