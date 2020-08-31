from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .models import PlatformUser, Expo, Contact, VisitantRegister, Stand
import datetime
from django.conf import settings
from .forms import ContactForm, EditExpoStaffForm, EditExpoOwnerForm, EditStandExpositorForm
from django.http import JsonResponse

@csrf_exempt
# Create your views here.
def home(request):
	if request.POST:
		form = ContactForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			email = form.cleaned_data['email']
			telefono = form.cleaned_data['telefono']
			interes = form.cleaned_data['interes']
			mensaje = form.cleaned_data['mensaje']
			NewContact = Contact()
			NewContact.nombre = nombre
			NewContact.email = email
			NewContact.telefono = telefono
			NewContact.mensaje = mensaje
			NewContact.interes = interes
			NewContact.save()
	form = ContactForm()
	return render(request, "Landing.html",{'form': form})

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
					return redirect('Expositor/SelectStand')
	return render(request, "Login.html")

@csrf_exempt
def createExpoStaff(request):
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
			return redirect('/Staff/SelectExpo');

	return render(request, "CreateExpo.html")

@csrf_exempt
def CreateOwnerUser(request):
	if request.POST:
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
		return redirect('/Staff/SelectExpo');

	return render(request, "CreateOwnerUser.html")

@csrf_exempt
def selectExpoStaff(request):
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
def selectStandExpositor(request):
	args = {}
	platformUser = PlatformUser.objects.get(user=request.user)
	args['stands'] = platformUser.user_stand.all()
	return TemplateResponse(request, "selectStandExpositor.html", args)

@csrf_exempt
def editStandExpositor(request, id_stand):
	selected_stand = Stand.objects.get(id=id_stand)
	if request.POST:
		form = EditStandExpositorForm(request.POST, request.FILES)
		if form.is_valid():
			temp_stand = Stand()
			temp_stand = form.save(commit=False)
			selected_stand.color1 = temp_stand.color1;
			selected_stand.color2 = temp_stand.color2;
			selected_stand.chat = temp_stand.chat;
			selected_stand.whatsapp = temp_stand.whatsapp;
			selected_stand.webpage = temp_stand.webpage;
			selected_stand.flyer_file = temp_stand.flyer_file;
			if 'logotipo' in request.FILES.keys():
				selected_stand.logotipo = request.FILES['logotipo'];
			if 'video_bienvenida' in request.FILES.keys():
				selected_stand.video_bienvenida = request.FILES['video_bienvenida'];
			if 'flyer_file' in request.FILES.keys():
				selected_stand.flyer_file = request.FILES['flyer_file'];
			if 'exhibition_video' in request.FILES.keys():
				selected_stand.exhibition_video = request.FILES['exhibition_video'];
			selected_stand.save();
			return redirect('/Expositor/EditStand/' + str(selected_stand.id));
	
	args = {}
	args['stand'] = selected_stand
	form = EditStandExpositorForm(instance = selected_stand)
	args['form'] = form
	return TemplateResponse(request, "EditStandExpositor.html", args)

@csrf_exempt
def editExpoStaff(request, expo_name):
	selected_expo = Expo.objects.get(nombre=expo_name)
	if request.POST:
		print(request.FILES)
		form = EditExpoStaffForm(request.POST, request.FILES)
		if form.is_valid():
			temp_expo = Expo()
			temp_expo = form.save(commit=False)
			selected_expo.nombre = temp_expo.nombre;
			selected_expo.stands_amount = temp_expo.stands_amount;
			if 'bannerA' in request.FILES.keys():
				selected_expo.bannerA = request.FILES['bannerA'];
			if 'bannerB' in request.FILES.keys():
				selected_expo.bannerB = request.FILES['bannerB'];
			if 'video' in request.FILES.keys():
				selected_expo.video = request.FILES['video'];
			selected_expo.save();
			return redirect('/Staff/EditExpo/' + selected_expo.nombre);
	
	args = {}
	args['expo'] = selected_expo
	args['expo'].fecha_final = str(args['expo'].fecha_final)
	args['expo'].fecha_inicio = str(args['expo'].fecha_inicio)
	args['expo'].hora_inicio = str(args['expo'].hora_inicio)
	args['expo'].hora_final = str(args['expo'].hora_final)
	
	form = EditExpoStaffForm(instance = selected_expo)
	args['form'] = form

	return TemplateResponse(request, "EditExpo.html", args)

@csrf_exempt
def editExpoOwner(request, expo_name):
	selected_expo = Expo.objects.get(nombre=expo_name)
	if request.POST:
		form = EditExpoOwnerForm(request.POST, request.FILES)
		if form.is_valid():
			temp_expo = Expo()
			temp_expo = form.save(commit=False)
			selected_expo.nombre = temp_expo.nombre;
			if 'bannerA' in request.FILES.keys():
				selected_expo.bannerA = request.FILES['bannerA'];
			if 'bannerB' in request.FILES.keys():
				selected_expo.bannerB = request.FILES['bannerB'];
			if 'video' in request.FILES.keys():
				selected_expo.video = request.FILES['video'];
			if 'TripticoPage1' in request.FILES.keys():
				selected_expo.TripticoPage1 = request.FILES['TripticoPage1'];
			if 'Calendario' in request.FILES.keys():
				selected_expo.Calendario = request.FILES['Calendario'];
			selected_expo.save();
			return redirect('/ExpoOwner/EditExpo/' + selected_expo.nombre);
	
	args = {}
	args['expo'] = selected_expo
	args['expo'].fecha_final = str(args['expo'].fecha_final)
	args['expo'].fecha_inicio = str(args['expo'].fecha_inicio)
	args['expo'].hora_inicio = str(args['expo'].hora_inicio)
	args['expo'].hora_final = str(args['expo'].hora_final)
	
	form = EditExpoOwnerForm(instance = selected_expo)
	args['form'] = form
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


@csrf_exempt
def appController(request, action):
	if request.POST:
		args = {}
		if action == "GetExpo":
			selected_expo = Expo.objects.get(nombre=request.POST['EXPO_NAME'])
			args['NAME'] = selected_expo.nombre
			args['BANNER_A'] = selected_expo.bannerA.url
			args['BANNER_B'] = selected_expo.bannerB.url
			args['TRIPTICO1'] = selected_expo.TripticoPage1.url
			args['CALENDARIO'] = selected_expo.Calendario.url
			args['VIDEO'] = selected_expo.video.url
			args['HALL1'] = selected_expo.Hall1
			args['HALL2'] = selected_expo.Hall2
			args['STATUS'] = 0
			return JsonResponse(args, safe=False);
		if action == "Register":
			selected_expo = Expo.objects.get(nombre=request.POST['EXPO_NAME'])
			visitant = VisitantRegister()
			visitant.name = request.POST['NAME']
			visitant.tel = request.POST['TEL']
			visitant.mail = request.POST['MAIL']
			visitant.related_expo = selected_expo
			visitant.save()
			args['STATUS'] = 0
			args['VISITANT_ID'] = visitant.id
			return JsonResponse(args, safe=False);

