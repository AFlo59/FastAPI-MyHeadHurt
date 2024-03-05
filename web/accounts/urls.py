from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('accounts/<str:username>/', views.username_page, name='username'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('validate_email/<uidb64>/<token>/', views.ValidateEmailView.as_view(), name='validate_email'),
    path('sendmail/<str:uidb64>/<str:token>/', views.ResendActivationEmailView.as_view(), name='sendmail'),
]