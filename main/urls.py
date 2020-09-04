from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import home, login, createExpoStaff, selectExpoStaff, editExpoStaff, editExpoOwner, selectExpoOwner, editExpoLayout, test, CreateOwnerUser, appController, selectStandExpositor, editStandExpositor, expoGL

urlpatterns = [
    path('', home, name = "home"),
    path('Login', login, name = "LoginStaff"),
    path('Staff/CreateExpo', createExpoStaff, name = "CreateExpo"),
    path('Staff/SelectExpo', selectExpoStaff, name = "SelectExpo"),
    path('Staff/EditExpo/<str:expo_name>/CreateOwnerUser', CreateOwnerUser, name = "CreateExpo"),
    path('Staff/EditExpo/<str:expo_name>', editExpoStaff, name = "EditExpo"),
    path('ExpoOwner/SelectExpo', selectExpoOwner, name = "SelectExpo"),
    path('ExpoOwner/Layout', home, name = "CreateExpo"),
    path('ExpoOwner/CreateExpositor', home, name = "CreateExpo"),
    path('ExpoOwner/EditExpo/layout', editExpoLayout, name = "EditExpo"),
    path('ExpoOwner/EditExpo/<str:expo_name>', editExpoOwner, name = "EditExpo"),

    path('Expositor/SelectStand', selectStandExpositor, name = "SelectStand"),
    path('Expositor/EditStand/<str:id_stand>', editStandExpositor, name = "EditStand"),
    path('expo/<str:expo_name>', expoGL, name = "test"),
    path('event/<str:expo_name>', test, name = "test"),
    path('page/<str:expo_name>', test, name = "test"),




    path('App/<str:action>', appController, name = "appController"),
]