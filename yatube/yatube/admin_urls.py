from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path("", admin.site.urls, name='wildcard'),
    path("logout/", views.index, name='index'),
]
