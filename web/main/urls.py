from django.urls import path
from main import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/<int:test>', views.contact_page, name='contact'),
    path('news/', views.news_page, name='news'),
]