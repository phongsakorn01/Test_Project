from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from WarehouseApp.models import Product,Employees,Transaction,Promotion

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('Productcode','ProductName','ProductQuantity')

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employees
        fields=('EmployeesId','EmployeesFullname')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transaction
        fields=('Transaction')

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Promotion
        fields=('No','PromotionCode','PromotionBeginDate','PromotionBeginTime','PromotionEndDate','PromotionEndTime')

