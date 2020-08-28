from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import home, login, createExpo, selectExpo, editExpo, editExpoOwner, selectExpoOwner, editExpoLayout, test;

urlpatterns = [
    path('', home, name = "home"),
    path('Login', login, name = "LoginStaff"),
    path('Staff/CreateExpo', createExpo, name = "CreateExpo"),
    path('Staff/SelectExpo', selectExpo, name = "SelectExpo"),
    path('Staff/AssignRoles', home, name = "CreateExpo"),
    path('Staff/EditExpo/<str:expo_name>', editExpo, name = "EditExpo"),
    path('ExpoOwner/SelectExpo', selectExpoOwner, name = "SelectExpo"),
    path('ExpoOwner/Layout', home, name = "CreateExpo"),
    path('ExpoOwner/CreateExpositor', home, name = "CreateExpo"),
    path('ExpoOwner/EditExpo/layout', editExpoLayout, name = "EditExpo"),
    path('ExpoOwner/EditExpo/<str:expo_name>', editExpoOwner, name = "EditExpo"),

    path('Expositor/SelectStand', home, name = "CreateExpo"),
    path('Expositor/EditStand', home, name = "CreateExpo"),
    path('test', test, name = "test"),
]