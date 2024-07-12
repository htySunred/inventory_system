from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from user.forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm


def register_page(request):
    form = CreateUserForm()
    # 添加完成 数据提交时发post，
    if request.method == 'POST':
        # 请求数据放到form的空表单中
        form = CreateUserForm(request.POST)
        # 判断数据有效
        if form.is_valid():
            # 保存
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'你成功创建了{username}的用户，继续登陆')
        else:
            messages.add_message(request, messages.WARNING, '未注册成功！可以重新再来！')
            # 重定向
        return redirect('user-login')
    #     是get
    else:
        # 进入注册面初始化，是空表
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'user/register.html', context=context)
def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request):

    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('user-profile')
    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'user/profile_update.html',context=context)
