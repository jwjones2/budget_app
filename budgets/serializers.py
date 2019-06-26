from budgets.models import Budget
from rest_framework import serializers

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Budget
        fields = ('id', 'name', 'description', 'end_date', 'purpose') 