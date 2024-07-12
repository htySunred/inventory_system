from django.contrib import admin
# 导入我们写models中的类
from .models import Product
from .models import Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','quantity']
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ['-created',]
    #fk_fields 设置显示外键字段
    fk_fields = ['category']
    # 指定名称name做为搜索字段
    search_fields = ['name']
    # 右侧栏过滤器，按作者进行筛选
    list_filter = ['category']
    # 详细时间分层筛
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'staff', 'product', 'order_quantity']
    list_per_page = 50
    list_filter = ['staff']
    ordering = ['-created']
    search_fields = ['product', 'staff']
    date_hierarchy = 'created'

admin.site.site_header = '商品库存交易仪表盘后台'
admin.site.site_title = '商品库存交易系统'