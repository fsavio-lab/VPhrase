from django.contrib import admin
from django.urls import path, include
from .views import (
    MovieListApiView
)

urlpatterns = [
    path('v1/movies/', MovieListApiView.as_view())
]
