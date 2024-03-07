from django.urls import path
from accounts.views import login, register, resend, views, validate, confirm, forgot
from django.contrib.auth.views import PasswordResetConfirmView

app_name = 'accounts'

urlpatterns = [
    path('login/', login.LoginView.as_view(), name='login'),
    path('register/', register.RegisterView.as_view(), name='register'),
    path('sendmail/<str:uidb64>/<str:token>/', resend.ResendActivationEmailView.as_view(), name='sendmail'),
    path('accounts/<str:username>/', views.username_page, name='username'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('confirm/<uidb64>/<token>/', confirm.confirm_email, name='confirm'),
    path('validate/<uidb64>/<token>/', validate.ValidateEmailView.as_view(), name='validate'),
    path('forgot-password/', forgot.forgot_password, name='forgot_password'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]