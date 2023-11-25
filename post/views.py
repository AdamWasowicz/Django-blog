from django.shortcuts import render
from django.views import View
from .forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse("post-index"))
            
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
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse("post-index"))
            
        return render(request, 'post/login_user.html', {
            'form': form
        })