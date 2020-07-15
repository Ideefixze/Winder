from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib import messages
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            
            username = form.cleaned_data.get('username')
            #new_user = authenticate(username=username,password=form.cleaned_data.get('password1'))
            #login(request, new_user)
            messages.success(request, f'Account created for {username}')
            return redirect('/')
    else:
        form = UserCreationForm()

    
    return render(request, 'register.html', {'form':form})


