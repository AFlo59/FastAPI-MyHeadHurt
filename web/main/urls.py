from django.urls import path
from main import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('special/', views.special_page, name='special'),
    path('contact/<int:test>', views.contact_page, name='contact'),
    path('api/', views.api_page, name='api'),
    path('api_predict/', views.api_predict_page, name='api-predict'),
]