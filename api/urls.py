from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from django.contrib import admin

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]