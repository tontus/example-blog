from django.http import Http404
from django.shortcuts import render

# LOGIN VIEW ENDPOINT
from authentication.forms import CreateUserForm


def login(request):
    return render(request, 'login.html')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
    return render(request, 'register.html', {'form': form})
