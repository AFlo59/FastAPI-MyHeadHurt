from django.urls import path
from accounts import views
from .views import SignUpView

app_name = 'accounts'

urlpatterns = [
    path('accounts/<str:username>/', views.username_page, name='accounts'),  # Corrected the view function name
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profil/', views.profil_page, name='profil'),
    # Add more URL patterns for login, logout, profile, etc., as needed
]