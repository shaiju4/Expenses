from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum
from .models import *
# Create your views here.



class CreateExpenses(ModelViewSet):
    serializer_class=ExpenseSerializer
    queryset=Expenses.objects.all()

    def create(self,request):
        '''method to save Expenses  .To keep commoon structure here using the response variable'''
        serializer=self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response={
                'status':status.HTTP_201_CREATED,
                "message":"Expense Created Successfully"
            }
            return Response(response,status=status.HTTP_201_CREATED)
            
        except Exception as e:
            response={
                'status':status.HTTP_400_BAD_REQUEST,
                "message":"Expense Creation Failed"
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        
        
    def list(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)
        try:
            data=self.get_queryset()
            serializer=ExpenseSerializer(data=data,many=True)
            response={
                "staus":status.HTTP_200_OK,
                "message":"Data Fetched Successfully",
                "data":serializer.data
                
            }
            return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
                response={
                    "staus":status.HTTP_400_BAD_REQUEST,
                    "message":"Something Went Wrong",
                    "error":serializer.errors    
                }
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
     
     

class FilterByMonthExpense(GenericAPIView):
    queryset=Expenses.objects.all()
    serializer_class=ExpenseSerializer
    def get(self,request,date):
        try:
            queryset=self.queryset
            filtered_data= queryset.filter(month=date).first()
            serializer=self.get_serializer(data=filtered_data)
            response={
                "staus":status.HTTP_200_OK,
                "message":"Data Fetched Successfully",
                "data":serializer.data    
            }
            return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            response={
                "staus":status.HTTP_400_BAD_REQUEST,
                "message":"Something Went Wrong",
                "error":serializer.errors    
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        
        

class GetToals(GenericAPIView):
    queryset=Expenses.objects.all()
    serializer_class=ExpenseSerializer
    def get(self):
        try:
            queryset=self.queryset
            expenses=queryset.aggregate(Sum('amount'))
            serializer=self.get_serializer(data=expenses)
            total_expenses=serializer(data=serializer.data)
            salarySerializer=SalarySerializer
            salarydata=SalaryPerMonth.objects.aggregate(Sum('salary'))
            total_salary=salarySerializer(data=salarydata)
            response={
                "status":status.HTTP_200_OK,
                "message":"Data Fetched Successfully",
                "data":{
                "total_salary":total_salary.data,
                "total_expenses":total_expenses 
                }
                
            }
            
            return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            response={
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"something went wrong",
                "error":str(e)
               
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
    