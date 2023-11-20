from django.shortcuts import render
from django.views import View
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, './post/index.html')
    

class CreateUserView(View):
    def get(self, request):
        form = UserForm()
        return render(request, './post/register_user.html', {
            'form': form
        })
    
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse("post-index"))
            
        return render(request, 'post/register_user.html', {
            'form': form
        })
