from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import datetime
from datetime import datetime
from django.utils.translation import gettext_lazy as _

class Expo(models.Model):
	nombre = models.CharField(max_length=80, null=True, blank=True)
	url = models.CharField(max_length=80, null=True, blank=True)
	fecha_inicio = models.DateField()
	fecha_final = models.DateField()
	hora_inicio = models.TimeField()
	hora_final = models.TimeField()
	bannerA = models.FileField(null=True, blank=True)
	bannerB = models.FileField(null=True, blank=True)
	video = models.FileField(null=True, blank=True)
	stands_amount = models.IntegerField()
	TripticoPage1 = models.FileField(null=True, blank=True)
	TripticoPage2 = models.FileField(null=True, blank=True)
	TripticoPage3 = models.FileField(null=True, blank=True)
	TripticoPage4 = models.FileField(null=True, blank=True)
	TripticoPage5 = models.FileField(null=True, blank=True)
	TripticoPage6 = models.FileField(null=True, blank=True)
	TripticoPage7 = models.FileField(null=True, blank=True)
	TripticoPage8 = models.FileField(null=True, blank=True)
	TripticoPage9 = models.FileField(null=True, blank=True)
	TripticoPage10 = models.FileField(null=True, blank=True)
	Calendario = models.FileField(null=True, blank=True)
	editKey = models.CharField(default="default", max_length=40, null=True, blank=True)
	Hall1 = models.TextField(default="default")
	Hall2 = models.TextField(default="default")

class ExpoDesign(models.Model):
	related_expo = models.ForeignKey(Expo, on_delete=models.CASCADE)
	class Meta:
		verbose_name = "ExpoDesign"
		verbose_name_plural = "ExpoDesigns"
	
	def __str__(self):
		pass

class VisitantRegister(models.Model):
	related_expo = models.ForeignKey(Expo, on_delete=models.CASCADE)

class Stand(models.Model):
	class PackageStand(models.TextChoices):
		BASIC = 'BAS', _('Basico')
		PLUS = 'PLS', _('Plus')
		GOLD = 'GOL', _('Gold')
		PLATINUM = 'PLA', _('Platinum')
		DIAMOND = 'DIA', _('Diamond')
	related_expo = models.ForeignKey(Expo, on_delete=models.CASCADE)
	nombre = models.CharField(default="default", max_length=40, null=True, blank=True)
	logotipo = models.FileField(null=True, blank=True)
	video_bienvenida = models.FileField(null=True, blank=True)
	whatsapp = models.CharField(max_length=80, null=True, blank=True)
	chat = models.CharField(max_length=80, null=True, blank=True)
	webpage = models.CharField(max_length=80, null=True, blank=True)
	flyer_file = models.FileField(null=True, blank=True)
	exhibition_video = models.FileField(null=True, blank=True)
	visitantes = models.ManyToManyField(VisitantRegister)
	editKey = models.CharField(default="default", max_length=40, null=True, blank=True)
	packageStand = models.CharField(
        max_length=3,
        choices=PackageStand.choices,
        default=PackageStand.BASIC
        )

class StandDesign(models.Model):
	related_stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
	standType = models.IntegerField()
	color1 = models.CharField(max_length=50)
	color2 = models.CharField(max_length=50)
	color3 = models.CharField(max_length=50)
	class Meta:
		verbose_name = "StandDesign"
		verbose_name_plural = "StandDesigns"
	def __str__(self):
		pass

class Eventos(models.Model):
	related_expo = models.ForeignKey(Expo, on_delete=models.CASCADE)
	Fecha = models.DateTimeField()
	redirect_url = models.CharField(max_length=100, null=True, blank=True)

class WelcomeWebpage(models.Model):	
	related_expo = models.ForeignKey(Expo, on_delete=models.CASCADE)

class PlatformUser(models.Model):
	class UserType(models.TextChoices):
		VISITOR = 'VIW', _('Visitante')
		STAND_OWNER = 'STO', _('Dueño de stand')
		EXPO_OWNER = 'EXO', _('Dueño de expo')
		STAFF = 'STF', _('Staff')
		ADMIN = 'ADM', _('Administrador')

	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(default="default", max_length=40, null=True, blank=True)
	user_expo = models.ForeignKey(Expo, on_delete=models.CASCADE, null=True, blank=True)
	user_stand = models.ForeignKey(Stand, on_delete=models.CASCADE, null=True, blank=True)
	user_type = models.CharField(
        max_length=3,
        choices=UserType.choices,
        default=UserType.VISITOR
    )


class Chat(models.Model):
	sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
	receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
	message = models.TextField(default="default")

class Feedback(models.Model):
	sender = models.ForeignKey(Expo, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
	message = models.TextField(default="default")

class Contact(models.Model):
	nombre = models.CharField(default="", max_length=80, null=True, blank=True)
	email = models.CharField(default="", max_length=80, null=True, blank=True)
	telefono = models.CharField(default="", max_length=80, null=True, blank=True)
	mensaje = models.TextField(default="", null=True, blank=True)
	interes = models.CharField(default="", max_length=40, null=True, blank=True)