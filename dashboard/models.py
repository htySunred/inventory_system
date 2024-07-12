from django.contrib.auth.models import User
from django.db import models

CATEGORY = (
    ('food', '食品'),
    ('mobile', '手机'),
    ('electronics', '电器'),
    ('book', '生活用品'),
    ('edutainment', '教育娱乐'),
    ('social_services', '社会服务'),
)


class Product(models.Model):
    name = models.CharField(verbose_name='产品名称', max_length=100, null=True)
    category = models.CharField(verbose_name='产品分类', max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(verbose_name='产品数量', null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = verbose_name
        ordering = ['-created']

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品', null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='员工')
    order_quantity = models.PositiveIntegerField(verbose_name='订单数量', null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name
        ordering = ['-created','staff']

    def __str__(self):
        return f'{self.staff}订{self.product}-{self.order_quantity}个'