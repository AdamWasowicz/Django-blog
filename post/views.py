from django.shortcuts import render
from django.views import View
from .forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, './post/index.html')
    

class RegisterUserView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, './post/register_user.html', {
            'form': form
        })
    
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            c_form = form.cleaned_data
            
            try:
                User.objects.get(email=c_form['email']).first()
                User.objects.get(username=c_form['username']).first()
            except:
                return render(request, 'post/register_user.html', {
                    'form': form,
                    'error_msg': "Email or username is already used"
                })
            
            new_user = User(
                username= c_form['username'],
                register_date= datetime.today(),
                email= c_form['email'],
                hashed_password= make_password(c_form['password'])
            )
            
            new_user.save()
            return HttpResponseRedirect(reverse("post-index"))
        
        else:    
            return render(request, 'post/register_user.html', {
                'form': form
            })


class LoginUserView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, './post/login_user.html', {
            'form': form
        })
    
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            c_form = form.cleaned_data
            
            try:
                user = User.objects.get(email=c_form["email"])
            except:
                return render(request, 'post/login_user.html', {
                    'form': form,
                    'error_msg': "Login or Password incorrect"
                })
            
            is_password_correct = check_password(c_form['password'], user.hashed_password)
            if is_password_correct == False:
                return render(request, 'post/login_user.html', {
                    'form': form,
                    'error_msg': "Login or Password incorrect"
                })
            
            return HttpResponseRedirect(reverse("post-index"))
            
        return render(request, 'post/login_user.html', {
            'form': form
        })