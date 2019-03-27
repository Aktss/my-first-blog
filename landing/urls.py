from django.conf.urls import url, include
from django.contrib import admin
from landing import views
from django.urls import path, include



urlpatterns = [
    url(r'^landing/', views.landing, name='landing')

]