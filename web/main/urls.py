from django.urls import path
from main import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('profil/', views.profil_page, name='profil'),
    path('contact/<int:test>', views.contact_page, name='contact'),
    path('predict/', views.predict_page, name='predict'),
    path('logout/', views.custom_logout, name='custom_logout'),
]