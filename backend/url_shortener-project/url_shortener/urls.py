from django.contrib import admin 
from django.urls import path, include 
from django.conf.urls import url 
from shortener.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/', ReactView.as_view()),
    path('add/', ReactView.as_view()),
]
