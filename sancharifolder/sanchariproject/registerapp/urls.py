from django.urls import path

from sanchariapp import views
from registerapp import views

urlpatterns = [

    path('register', views.registerin, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout")
]
