"""inventory_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('demo/', views.demo1, name='dashboard-demo'),
    path('product/', views.product_list, name='dashboard-product'),
    path('product/delete/<int:pk>', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>', views.product_update, name='dashboard-product-update'),
    path('order/', views.order_list, name='dashboard-order'),
    path('order/delete/<int:pk>', views.order_delete, name='dashboard-order-delete'),
    path('order/update/<int:pk>', views.order_update, name='dashboard-order-update'),
]
