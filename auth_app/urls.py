from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='auth_app-index'),
    path('register', views.RegisterUserView.as_view(), name='auth_app-user-register'),
    path('login', views.LoginUserView.as_view(), name='auth_app-user-login')
]
