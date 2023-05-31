from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .forms import ConsultantProfileForm
from .models import ProfileConsultant
from . import utils
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    profile_or_none = utils.get_profile_or_none(request)
    if profile_or_none is None:
        messages.error(request, 'Для начала работы создайте профиль')
        return redirect('users:edit_profile') 
    else:
        context = utils.get_profile_context(request)
        template = utils.get_template_profile(request)
        return render(request, template, context)

@login_required
def edit_profile(request):
    UserForm = utils.get_profile_forms(request)
    if request.method =="POST":
        profile = utils.get_profile_user(request)
        profile_form = UserForm(request.POST,request.FILES, instance=profile)  
        if profile_form.is_valid():
            check = profile_form.save()
            # check.user = request.user
            # check.save()
            messages.success(request, 'Ваш профиль успешно обновлен.')
            return redirect('users:profile') 
    profile_or_none = utils.get_profile_or_none(request)
    if profile_or_none:
        form = UserForm(instance=profile_or_none)
    else:
        form = UserForm()
    return render(request, 'users/edit_profile.html', {'form':form})

@login_required
def activate_profile(request):
    if hasattr(request.user,'profileconsultant'):
        profile_object = request.user.profileconsultant
        profile_object.is_activate = not profile_object.is_activate
        profile_object.save()
    return redirect('users:profile')  