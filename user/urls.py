from django.urls import path
from user import views

urlpatterns = [
    path('welcome', views.welcome , name="welcome"),
    path('register', views.register, name="register"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout, name="logout"),
]