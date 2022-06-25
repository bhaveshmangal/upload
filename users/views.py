from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('files')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username= username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'users/login-register.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'User was logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'New user created')
            login(request, user)
            return redirect('edit-account')
        else:
            messages.warning(request, 'An error has occurred during registration')
    context = {'page': page, 'form': form}
    return render(request, 'users/login-register.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance = profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)