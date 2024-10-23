from django.db import models

# Create your models here.


class Expenses(models.Model):
    name=models.CharField(max_length=100)
    amount=models.FloatField()
    category=models.CharField(max_length=100)
    month=models.DateField()
    
    
class SalaryPerMonth(models.Model):
    month=models.DateField()
    salary=models.IntegerField()
    
    
 
    