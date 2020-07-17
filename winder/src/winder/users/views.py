from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import messages
from .models import Profile
from .forms import ProfileSettingsForm
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            profile=Profile(user=new_user,first_name="Anonymous",last_name="Anonymous")
            profile.save()
            username = form.cleaned_data.get('username')
            #new_user = authenticate(username=username,password=form.cleaned_data.get('password1'))
            #login(request, new_user)
            messages.success(request, f'Account created for {username}')
            return redirect('/')
    else:
        form = UserCreationForm()

    
    return render(request, 'register.html', {'form':form})

@login_required
def profile_view(request):
    user_data = Profile.objects.get(user__username=request.GET.get('user'))
    return render(request, 'profile.html', {'user_data':user_data})


@login_required
def settings_view(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=="POST":
        form = ProfileSettingsForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Settings saved!')
            return redirect('/')
    else:
        #form = ProfileSettingsForm(initial={'first_name':profile.first_name, 'last_name':profile.last_name, 'profile_picture':profile.profile_picture})
        form = ProfileSettingsForm(instance=profile)
    
    return render(request, 'settings.html', {'form':form})
