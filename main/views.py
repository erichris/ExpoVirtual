from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .models import PlatformUser, Expo, Contact
import datetime
from django.conf import settings



@csrf_exempt
# Create your views here.
def home(request):
	if request.POST:
		if request.POST['Action'] == "Contact":
			nombre = request.POST['nombreForm']
			correo = request.POST['correoForm']
			telefono = request.POST['telefonoForm']
			interes = request.POST['interes']
			mensaje = request.POST['mensajeForm']
			NewContact = Contact()
			NewContact.nombre = nombre
			NewContact.email = correo
			NewContact.telefono = telefono
			NewContact.mensaje = mensaje
			NewContact.interes = interes
			NewContact.save()
	return render(request, "Landing.html")

@csrf_exempt
def login(request):
	if request.POST:
		if request.POST['Action'] == "Login":
			username = request.POST['user']
			password = request.POST['pass']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				platformUser = PlatformUser.objects.filter(user=user).first()
				if platformUser.user_type == "ADM":
					return redirect('admin/')
				elif platformUser.user_type == "STF":
					return redirect('Staff/SelectExpo')
				elif platformUser.user_type == "EXO":
					return redirect('ExpoOwner/SelectExpo')
				elif platformUser.user_type == "STO":
					return redirect('admin/')
	return render(request, "Login.html")

@csrf_exempt
def createExpo(request):
	if request.POST:
		if request.POST['Action'] == "CreateExpo":
			numero_stands = request.POST['numeroStands']
			nombre_expo = request.POST['nombreExpo']
			datetime_inicio = request.POST['HoraInicio'].replace('T', ' ')
			datetime_fin = request.POST['HoraFin'].replace('T', ' ')
			datetime_inicio_obj = datetime.datetime.strptime(datetime_inicio, '%Y-%m-%d %H:%M')
			datetime_fin_obj = datetime.datetime.strptime(datetime_fin, '%Y-%m-%d %H:%M')
			NewExpo = Expo()
			NewExpo.nombre = nombre_expo;
			NewExpo.fecha_inicio = datetime_inicio_obj.date()
			NewExpo.fecha_final = datetime_fin_obj.date()
			NewExpo.hora_inicio = datetime_inicio_obj.time()
			NewExpo.hora_final = datetime_fin_obj.time()
			NewExpo.stands_amount = numero_stands
			NewExpo.save()

	return render(request, "CreateExpo.html")

@csrf_exempt
def selectExpo(request):
	args = {}
	args['expos'] = Expo.objects.all()
	args['url_new_expo'] = "CreateExpo"
	return TemplateResponse(request, "SelectExpo.html", args)

@csrf_exempt
def selectExpoOwner(request):
	args = {}
	platformUser = PlatformUser.objects.get(user=request.user)
	args['expos'] = platformUser.user_expo.all()
	return TemplateResponse(request, "SelectExpoOwner.html", args)

@csrf_exempt
def editExpo(request, expo_name):
	args = {}
	args['expo'] = Expo.objects.get(nombre=expo_name)
	args['expo'].fecha_final = str(args['expo'].fecha_final)
	args['expo'].fecha_inicio = str(args['expo'].fecha_inicio)
	args['expo'].hora_inicio = str(args['expo'].hora_inicio)
	args['expo'].hora_final = str(args['expo'].hora_final)
	return TemplateResponse(request, "EditExpo.html", args)

@csrf_exempt
def editExpoOwner(request, expo_name):
	args = {}
	args['expo'] = Expo.objects.get(nombre=expo_name)
	args['expo'].fecha_final = str(args['expo'].fecha_final)
	args['expo'].fecha_inicio = str(args['expo'].fecha_inicio)
	args['expo'].hora_inicio = str(args['expo'].hora_inicio)
	args['expo'].hora_final = str(args['expo'].hora_final)
	return TemplateResponse(request, "EditExpoOwner.html", args)


def editExpoLayout(request):
	args = {}
	platformUser = PlatformUser.objects.get(user=request.user)
	args['expos'] = platformUser.user_expo.all()
	return TemplateResponse(request, "SelectExpoOwner.html", args)

@csrf_exempt
# Create your views here.
def test(request):
	return render(request, "test.html")