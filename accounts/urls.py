from django.urls import path
from . import views

app_name = 'accounts'  # names the app for urls, i.e. accounts:signup for /accounts/signup

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login')
]
