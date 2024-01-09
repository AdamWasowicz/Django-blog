from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, LoginForm
from django.contrib import messages


class IndexView(View):
    def get(self, request):
        return render(request, './auth_app/index.html')



class RegisterUserView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, './auth_app/register_user.html', {
            'form': form
        })
        
    
    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_app-user-login')
        else:
            return render(request, './auth_app/register_user.html', {
                'form': form
            })



class LoginUserView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, './auth_app/login_user.html', {
            'form': form
        })
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('auth_app-index')
        else:
            form = LoginForm(request.POST)
            return render(request, './auth_app/login_user.html', {
                'form': form,
                'errorMsg': 'Error'
            })