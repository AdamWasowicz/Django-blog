from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='post-index'),
    path('register', views.RegisterUserView.as_view(), name='post-user-register'),
    path('login', views.LoginUserView.as_view(), name='post-user-login')
]
