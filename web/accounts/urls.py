from django.urls import path
from accounts.views import login, register, resend, views, forgot, activate
from django.contrib.auth.views import PasswordResetConfirmView

app_name = 'accounts'

urlpatterns = [
    path('login/', login.LoginView.as_view(), name='login'),
    path('register/', register.RegisterView.as_view(), name='register'),
    path('accounts/<str:username>/', views.username_page, name='username'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('sendmail/<str:uidb64>/<str:token>/', resend.ResendActivationEmailView.as_view(), name='sendmail'),
    path('activate/<str:uidb64>/<str:token>/', activate.activate_account, name='activate'),
    path('forgot-password/', forgot.forgot_password, name='forgot_password'),
    path('reset/<uidb64>/<token>/', forgot.reset_password_confirm, name='password_reset_confirm'),

]