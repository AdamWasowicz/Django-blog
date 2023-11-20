from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='post-index'),
    path('register', views.CreateUserView.as_view(), name='post-register')
]
