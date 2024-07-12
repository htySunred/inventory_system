from django.contrib.auth.models import User
from django.db import models


class profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField("地址", max_length=200, null=True)
    phone = models.CharField("电话", max_length=50, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='Profile_Images')


    def __str__(self):
        # 关系 表字段调用
        return f'{self.staff.username}'
