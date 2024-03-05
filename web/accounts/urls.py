from django.urls import path
from accounts.views import login, register, resend, views


app_name = 'accounts'

urlpatterns = [
    path('login/', login.LoginView.as_view(), name='login'),
    path('register/', register.RegisterView.as_view(), name='register'),
    path('sendmail/<str:uidb64>/<str:token>/', resend.ResendActivationEmailView.as_view(), name='sendmail'),
    path('accounts/<str:username>/', views.username_page, name='username'),
    path('logout/', views.custom_logout, name='custom_logout'),
]