from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    progress_percentage = serializers.ReadOnlyField()

    class Meta:
        model = Goal
        fields = ['id', 'name', 'target_amount', 'current_amount', 'deadline', 'status', 'progress_percentage', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        if 'target_amount' in data and data['target_amount'] <= 0:
            raise serializers.ValidationError("Target amount must be greater than zero.")
        if 'current_amount' in data and data['current_amount'] < 0:
            raise serializers.ValidationError("Current amount cannot be negative.")
        if 'current_amount' in data and 'target_amount' in data and data['current_amount'] > data['target_amount']:
            raise serializers.ValidationError("Current amount cannot exceed target amount.")
        return data