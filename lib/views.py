from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from .models import Password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .form import RegistrationForm, PasswordForm
from django.contrib.auth.decorators import login_required


@login_required
def CreatePassword(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('profile')
    else:
        form = PasswordForm()
    context = {'form': form}

    return render(request, 'create.html', context)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, 'register.html', context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, 'login.html', context)


@login_required
def Profile(request):
    search = request.GET.get("search")
    if search:
        allofuser = Password.objects.filter(address__icontains=search)
    else:
        allofuser = Password.objects.all().order_by('-id')

    context = {'userof': allofuser}

    return render(request, 'profile.html', context)


def Detail(request, pk):
    detail = Password.objects.get(pk=pk)

    context = {"detail": detail}
    return render(request, 'detail.html', context)
