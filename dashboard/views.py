from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product,Order
from .forms import ProductForm,OrderForm


@login_required(login_url='')
def index(request):
    workers = User.objects.all()
    workers_count = workers.count()
    items = Product.objects.all()
    products_count = items.count()
    orders = Order.objects.all()
    orders_count = orders.count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            ins=form.save(commit=False)
            ins.staff=request.user
            ins.save()
            product_name = form.cleaned_data.get('product')
            messages.success(request, f'你成功更新了{product_name}')
        return redirect('dashboard-index')
    else:
        form = OrderForm()
    context={
        'products':items,
        'form':form,
        'orders': orders,
        'workers_count': workers_count,
        'products_count': products_count,
        'orders_count': orders_count,
    }
    return render(request, 'dashboard/index.html',context=context)


@login_required(login_url='')
def staff(request):
    # 从数据库user表取回数据给变量workers，
    workers = User.objects.all()
    workers_count = workers.count()
    items = Product.objects.all()
    products_count = items.count()
    orders = Order.objects.all()
    orders_count = orders.count()


    context={'workers':workers,
              'workers_count':workers_count,
               'products_count':products_count,
               'orders_count':orders_count,
             }
    # 返回workers给前端网页
    return render(request, 'dashboard/staff.html',context=context)

def staff_detail(request,pk):
    worker=User.objects.get(id=pk)
    context={'worker':worker}
    return render(request, 'dashboard/staff_detail.html',context)

@login_required(login_url='')
def product_list(request):
    form = ProductForm()
    workers = User.objects.all()
    workers_count = workers.count()
    items=Product.objects.all()
    products_count=items.count()
    orders = Order.objects.all()
    orders_count=orders.count()
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'你成功更新了{product_name}')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    # 拼接表单和数据
    context = {'form': form,
               'items':items,
               'workers_count':workers_count,
               'products_count':products_count,
               'orders_count':orders_count,
               }
    #拼接后返回前端，指向具体html
    return render(request, 'dashboard/product.html', context=context)


# 从前面传数据
@login_required(login_url='')
def product_delete(request,pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    context = {'item': item}
    return render(request, 'dashboard/product_delete.html', context=context)

@login_required(login_url='')
def product_update(request,pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
       #  前端数据request+数据库 item
       form=ProductForm(request.POST,instance=item)
       if form.is_valid():
           form.save()
           product_name = form.cleaned_data.get('name')
           messages.success(request, f'你成功更新了{product_name}')

           return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)

    context = {
        'form': form,

    }
    return render(request, 'dashboard/product_update.html', context)


@login_required(login_url='')
def order_list(request):
    workers = User.objects.all()
    workers_count = workers.count()
    items = Product.objects.all()
    products_count = items.count()
    orders = Order.objects.all()
    orders_count = orders.count()
    context={
        'orders':orders,
        'workers_count': workers_count,
        'products_count': products_count,
        'orders_count': orders_count,
    }
    return render(request, 'dashboard/order.html',context=context)


@login_required(login_url='')
def order_delete(request,pk):
    item = Order.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-index')
    context = {'item': item}
    return render(request, 'dashboard/order_delete.html', context=context)

@login_required(login_url='')
def order_update(request,pk):
    item=Order.objects.get(id=pk)
    if request.method=='POST':
       #  前端数据request+数据库 item
       form=OrderForm(request.POST,instance=item)
       if form.is_valid():
           form.save()
           product_name = form.cleaned_data.get('product')
           messages.success(request, f'你成功更新了{product_name}')

           return redirect('dashboard-index')
    else:
        form = OrderForm(instance=item)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/order_update.html', context)




def demo1(request):
    return render(request, 'dashboard/demo.html')
