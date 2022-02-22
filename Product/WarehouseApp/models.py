from enum import unique
from django.db import models
from django.forms import CharField

# Create your models here.
class Product(models.Model):
    Productcode = models.AutoField(primary_key = True )
    ProductName = models.CharField(max_length = 500 )
    ProductQuantity = models.IntegerField()
class Employees(models.Model):
    EmployeesId = models.AutoField(primary_key = True)
    EmployeesFullname = models.CharField(max_length = 500 )
    
class Transaction(models.Model):
    Transaction = CharField(max_length = 500 )

class Promotion(models.Model):
    No = models.AutoField(primary_key = True)
    PromotionCode = models.CharField(max_length= 500)
    PromotionBeginDate = models.DateField()
    PromotionBeginTime = models.TimeField()
    PromotionEndDate = models.DateField()
    PromotionEndTime  = models.TimeField()


