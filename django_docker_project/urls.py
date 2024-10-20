# my_django_project/urls.py
from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),           # Home page
    path('about/', views.about, name='about'),   # About page
    path('contact/', views.contact, name='contact'), # Contact page
]
