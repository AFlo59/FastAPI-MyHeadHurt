from django.contrib import admin
from django.urls import path, include
from accounts import views
from functionalities import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('functionalities.urls')),
    path("accounts/", include("accounts.urls"))
]