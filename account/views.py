from django.shortcuts import render
from .forms import RegForm, SetUserForm, SetProfileForm
from .models import Profile
from core_logic.models import Wallet
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def registration(request):
    if request.method == 'POST':
        user_form = RegForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            Wallet.objects.create(user=Profile.objects.get(user=new_user))
            return redirect('login/')
        else:
            return render(request,
                    'registration/main.html',
                    {'user_form':user_form,})
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        user_form = RegForm()
        return render(request,
                    'registration/main.html',
                    {'user_form':user_form,
                    'error': False})

@login_required
def settings(request):
    if request.method == 'POST':
        set_user_form = SetUserForm(instance=request.user,
                                data=request.POST)
        set_prof_form = SetProfileForm(
                                instance=request.user.profile,
                                data=request.POST,
                                files=request.FILES)
        if set_user_form.is_valid() and set_prof_form.is_valid():
            set_user_form.save()
            set_prof_form.save()
            return redirect('settings')
    else:
        set_user_form = SetUserForm(instance=request.user)
        set_prof_form = SetProfileForm(instance=request.user.profile)
        return render(request,
                'account/settings.html',
                {'set_user_form': set_user_form,
                'set_prof_form': set_prof_form})

