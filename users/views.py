from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created successfully! Welcome, {user_name}')
            return redirect('myapp:events')
    else:
        form = SignupForm()
    return render(request,'users/register.html',{'form':form})