from django.shortcuts import render
from .forms import RegForm
from .models import Profile
from django.shortcuts import redirect

# Create your views here.
def registration(request):
    if request.method == 'POST':
        user_form = RegForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            print(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('login/')
    else:
        user_form = RegForm()
        return render(request,
                    'registration/main.html',
                    {'user_form':user_form})