from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index-page')  # Перенаправление на главную страницу после успешной регистрации
    else:
        form = RegistrationForm()
    return render(request, 'blablacar/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index-page')
            else:
                form.add_error(None, 'Неверные учетные данные')
    else:
        form = LoginForm()
    return render(request, 'blablacar/login.html', {'form': form})


