import code
import re
from telnetlib import EL
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from WarehouseApp.models import Product,Employees,Transaction,Promotion
from WarehouseApp.serializers import ProductSerializer,EmployeesSerializer,TransactionSerializer,PromotionSerializer


# Create your views here.
@csrf_exempt
def productAPI(request,id = 0):
    if request.method == ('GET'):
        product = Product.objects.all()
        product_serializer = ProductSerializer(product,many = True)
        return JsonResponse(product_serializer.data,safe = False)
    elif request.method == ('POST'):
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data = product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully",safe=False )
        return JsonResponse("Failed to Add",safe= False)
    elif request.method == ('PUT'):
        product_data = JSONParser().parse(request)
        product = Product.objects.get(Productcode = product_data['Productcode'])
        product_serializer = ProductSerializer(product,data = product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Update Successfully",safe= False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        product = Product.objects.get(Productcode=id)
        product.delete()
        return JsonResponse("Deleted Succesfully",safe=False)
    
    
@csrf_exempt
def employeesAPI(request,id = 0):
    if request.method == ('GET'):
        employees =Employees.objects.all()
        employees_serializer = EmployeesSerializer(employees,many = True)
        return JsonResponse(employees_serializer.data,safe = False)
    elif request.method == ('POST'):
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeesSerializer(data = employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False )
        return JsonResponse("Failed to Add",safe= False)
    elif request.method == ('PUT'):
        employees_data = JSONParser().parse(request)
        employees = Employees.objects.get(EmployeesId = employees_data['EmployeesId'])
        employees_serializer = EmployeesSerializer(employees,data = employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Successfully",safe= False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        employees = Employees.objects.get(EmployeesId=id)
        employees.delete()
        return JsonResponse("Deleted Succesfully",safe=False)
    

@csrf_exempt
def promotionAPI(request,id = 0):
    if request.method == ('GET'):
        promotion =Promotion.objects.all()
        promotion_serializer = PromotionSerializer(promotion,many = True)
        return JsonResponse(promotion_serializer.data,safe = False)
    elif request.method == ('POST'):
        promotion_data = JSONParser().parse(request)
        promotion_serializer = PromotionSerializer(data = promotion_data)
        if promotion_serializer.is_valid():
            promotion_serializer.save()
            return JsonResponse("Added Successfully",safe=False )
        return JsonResponse("Failed to Add",safe= False)
    elif request.method == ('PUT'):
        promotion_data = JSONParser().parse(request)
        promotion = Promotion.objects.get(PromotionCode = promotion_data['PromotionCode'])
        promotion_serializer = PromotionSerializer(promotion,data = promotion_data)
        if promotion_serializer.is_valid():
            promotion_serializer.save()
            return JsonResponse("Update Successfully",safe= False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        promotion = Promotion.objects.get(No=id)
        promotion.delete()
        return JsonResponse("Deleted Succesfully",safe=False)
    

