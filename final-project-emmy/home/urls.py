from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('login', views.login_request, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_request, name="logout"),
]
