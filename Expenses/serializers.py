from .models import *
from rest_framework.serializers import Serializer,ModelSerializer

class ExpenseSerializer(ModelSerializer):
    
    class Meta:
        model=Expenses
        fields=[
            'name','expense','category'
        ]
    
    

class SalarySerializer(ModelSerializer):
    
    class Meta:
        model=SalaryPerMonth
        fields="__all__"