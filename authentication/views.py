from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import render, redirect

# LOGIN VIEW ENDPOINT
from authentication.forms import CreateUserForm


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print('hmm')
            return redirect('home')
        else:
            print('dsfassssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss')
    return render(request, 'login.html')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    return render(request, 'register.html', {'form': form})
