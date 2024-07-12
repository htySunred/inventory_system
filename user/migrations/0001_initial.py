# Generated by Django 4.2.13 on 2024-07-05 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='地址')),
                ('phone', models.CharField(max_length=50, null=True, verbose_name='电话')),
                ('image', models.ImageField(default='avatar.jpg', upload_to='Profile_Images')),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '客户详细信息',
                'verbose_name_plural': '客户详细信息',
            },
        ),
    ]
