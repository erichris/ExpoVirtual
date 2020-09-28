from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import home, loginW, createExpoStaff, selectExpoStaff, editExpoStaff, editExpoOwner, selectExpoOwner, editExpoLayout, test, CreateOwnerUser, appController, selectStandExpositor, editStandExpositor, expoGL, layout, createExpoOwner, editUserExpoOwner, editUserStandOwner, createStandOwner, editStandExpoOwner, createStandExpoOwner, eventGL, export_asistentes_csv

urlpatterns = [
    path('', home, name = "home"),
    path('Login', loginW, name = "LoginStaff"),
    path('Staff/CreateExpo', createExpoStaff, name = ""),
    path('Staff/SelectExpo', selectExpoStaff, name = ""),
    path('Staff/EditExpo/<str:expo_name>/CreateOwnerUser', CreateOwnerUser, name = ""),
    path('Staff/EditExpo/<str:expo_name>', editExpoStaff, name = ""),
    path('Staff/EditExpoOwner/<str:id>', editUserExpoOwner, name = ""),
    path('Staff/CreateExpositor', createExpoOwner, name = ""),
    path('ExpoOwner/SelectExpo', selectExpoOwner, name = ""),
    path('ExpoOwner/Layout/<str:expo_name>', layout, name = ""),
    path('ExpoOwner/CreateExpositor', createStandOwner, name = ""),
    path('ExpoOwner/EditExpo/CreateStand/<str:id>', createStandExpoOwner, name = ""),
    path('ExpoOwner/EditExpo/layout', editExpoLayout, name = ""),
    path('ExpoOwner/EditExpo/<str:expo_name>', editExpoOwner, name = ""),
    path('ExpoOwner/EditExpoOwner/<str:id>', editUserStandOwner, name = ""),
    path('ExpoOwner/StandEdit/<str:id>', editStandExpoOwner, name = ""),
    

    path('Expositor/SelectStand', selectStandExpositor, name = ""),
    path('Expositor/EditStand/<str:id_stand>', editStandExpositor, name = ""),
    path('expo/<str:expo_name>', expoGL, name = ""),
    path('event/<str:expo_name>', eventGL, name = ""),
    path('page/<str:expo_name>', test, name = ""),
    path('estadisticas', export_asistentes_csv, name = ""),




    path('App/<str:action>', appController, name = "appController"),
]
