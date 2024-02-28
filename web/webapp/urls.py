from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
    path('funct/', include('functionalities.urls')),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls"))
]