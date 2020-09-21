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

	bannerWebpage = models.FileField(null=True, blank=True)

	Carrusel1 = models.FileField(null=True, blank=True)
	Carrusel2 = models.FileField(null=True, blank=True)
	Carrusel3 = models.FileField(null=True, blank=True)
	Carrusel4 = models.FileField(null=True, blank=True)
	Carrusel5 = models.FileField(null=True, blank=True)
	Patrocinador1 = models.FileField(null=True, blank=True)
	Patrocinador2 = models.FileField(null=True, blank=True)
	Patrocinador3 = models.FileField(null=True, blank=True)
	Patrocinador4 = models.FileField(null=True, blank=True)
	Patrocinador5 = models.FileField(null=True, blank=True)
	Patrocinador6 = models.FileField(null=True, blank=True)
	Patrocinador7 = models.FileField(null=True, blank=True)
	Patrocinador8 = models.FileField(null=True, blank=True)
	Patrocinador9 = models.FileField(null=True, blank=True)
	Patrocinador10 = models.FileField(null=True, blank=True)

	facebook = models.CharField(max_length=80, null=True, blank=True)
	instagram = models.CharField(max_length=80, null=True, blank=True)
	youtube = models.CharField(max_length=80, null=True, blank=True)

	editKey = models.CharField(default="default", max_length=40, null=True, blank=True)
	Hall1 = models.TextField(default="default")
	Hall2 = models.TextField(default="default")

	def __str__(self):
		return self.nombre

class ExpoDesign(models.Model):
	related_expo = models.ForeignKey(Expo, on_delete=models.CASCADE)
	class Meta:
		verbose_name = "ExpoDesign"
		verbose_name_plural = "ExpoDesigns"
	
	def __str__(self):
		return self.related_expo.nombre

class VisitantRegister(models.Model):
	name = models.CharField(max_length=80, null=True, blank=True)
	tel = models.CharField(max_length=80, null=True, blank=True)
	mail = models.CharField(max_length=80, null=True, blank=True)
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
	banner1 = models.FileField(null=True, blank=True)
	banner2 = models.FileField(null=True, blank=True)
	banner3 = models.FileField(null=True, blank=True)
	banner4 = models.FileField(null=True, blank=True)
	banner5 = models.FileField(null=True, blank=True)
	banner6 = models.FileField(null=True, blank=True)
	banner_horizontal1 = models.FileField(null=True, blank=True)
	banner_horizontal2 = models.FileField(null=True, blank=True)
	banner_horizontal3 = models.FileField(null=True, blank=True)
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
	standType = models.IntegerField(default=0)
	color1 = models.CharField(max_length=50, null=True, blank=True)
	color2 = models.CharField(max_length=50, null=True, blank=True)
	position = models.CharField(max_length=50, null=True, blank=True)
	def __str__(self):
		return self.nombre

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
	first_login = models.BooleanField(default=True)
	user_expo = models.ManyToManyField(Expo, blank=True)
	user_stand = models.ManyToManyField(Stand, blank=True)
	user_type = models.CharField(
        max_length=3,
        choices=UserType.choices,
        default=UserType.VISITOR)
	def __str__(self):
		if self.user != None:
			return self.user.username
		return "No name";

class Chat(models.Model):
	sender = models.CharField(default="", max_length=20, null=True, blank=True)
	receiver = models.CharField(default="", max_length=20, null=True, blank=True)
	message = models.TextField(default="default")
	senderIsSender = models.BooleanField(default=True, null=True, blank=True)

class Feedback(models.Model):
	related_expo = models.ForeignKey(Expo, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
	sender = models.ForeignKey(VisitantRegister, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
	message = models.TextField(default="default")

class Contact(models.Model):
	nombre = models.CharField(default="", max_length=80, null=True, blank=True)
	email = models.CharField(default="", max_length=80, null=True, blank=True)
	telefono = models.CharField(default="", max_length=80, null=True, blank=True)
	mensaje = models.TextField(default="", null=True, blank=True)
	interes = models.CharField(default="", max_length=40, null=True, blank=True)