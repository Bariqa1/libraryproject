from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Task 1: Register View
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Task 5: رسالة نجاح
            messages.success(request, 'You have successfully registered!')
            return redirect('login_user') # يوجهنا لصفحة الدخول
    else:
        form = UserCreationForm()
    return render(request, 'usermodule/register.html', {'form': form})

# Task 2: Login View
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Task 5: رسالة نجاح
                messages.success(request, f'Welcome {username}, login successful!')
                return redirect('list_students') # يوجهنا للصفحة الرئيسية بعد الدخول
    else:
        form = AuthenticationForm()
    
    return render(request, 'usermodule/login.html', {'form': form})

# Task 4: Logout View
def logout_user(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login_user')