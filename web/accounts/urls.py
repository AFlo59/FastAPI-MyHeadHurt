from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/<str:username>/', views.accounts_page, name='accounts'),
]