# accounts/urls.py

from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/<str:username>/', views.username_page, name='accounts'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profil/', views.profil_page, name='profil'), 
    path('logout/', views.custom_logout, name='custom_logout'), # Make sure this line is present
    # Add more URL patterns for login, logout, profile, etc., as needed
]