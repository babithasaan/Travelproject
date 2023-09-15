from django.urls import path

from sanchariapp import views

urlpatterns = [

    path('', views.demo, name="demo")
]
