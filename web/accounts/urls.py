from django.urls import path
from . import views
from accounts.views import *


app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('accounts/<str:username>/', views.username_page, name='username'),
    path('logout/', custom_logout, name='custom_logout'),
    path('validate_email/<str:uidb64>/<str:token>/', ValidateEmailView.as_view(), name='validate_email'),
]
