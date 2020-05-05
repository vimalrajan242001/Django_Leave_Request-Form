
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout',views.logout,name='logout')

]