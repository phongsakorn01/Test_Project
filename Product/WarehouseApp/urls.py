
from django.urls import re_path
from WarehouseApp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    re_path(r'^product$',views.productAPI),
    re_path(r'^product/([0-9]+)$',views.productAPI),

    re_path(r'^employees$',views.employeesAPI),
    re_path(r'^employees/([0-9]+)$',views.employeesAPI),

    re_path(r'^promotion$',views.promotionAPI),
    re_path(r'^promotion/([0-9]+)$',views.promotionAPI)


]