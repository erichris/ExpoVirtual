from django import forms
from django.forms import ModelForm, Textarea, TextInput, MultipleChoiceField, Select
from .models import Contact, Expo, Stand, PlatformUser
from django.contrib.auth.models import User

class ContactForm(ModelForm):
	class Meta:
		OPTIONS = (
	        ("Eventos", "Eventos"),
	        ("Paquetes y precios", "Paquetes y precios"),
        )
		model = Contact
		fields = ('nombre', 'email', 'telefono', 'mensaje', 'interes')
		widgets = {
			'nombre': TextInput(attrs={'class':'InputText ContactFormElement', 'placeholder': 'Nombre...'}),
			'email': TextInput(attrs={'class':'InputText ContactFormElement', 'placeholder': 'Correo...'}),
			'telefono': TextInput(attrs={'class':'InputText ContactFormElement', 'placeholder': 'Telefono...'}),
			'mensaje': Textarea(attrs={'cols': 30, 'rows': 2, 'class':'InputText ContactTextArea', 'placeholder': 'Mensaje...'}),
			'interes': Select(attrs={'class':'InputText ContactFormElement', 'placeholder': 'Nombre...'}, choices=OPTIONS),
		}

class EditExpoStaffForm(ModelForm):
	class Meta:
		OPTIONS = (
	        ("40", "40"),
	        ("80", "80"),
	        ("120", "120")
        )
		model = Expo
		fields = ('nombre', 'bannerA', 'bannerB', 'video', 'stands_amount' )
		widgets = {
			'stands_amount': Select(choices=OPTIONS),
			#'bannerA': TextInput(attrs={'class':'custom-file-input InputText ContactFormElement', 'type': 'file'}),
		}
		labels = {
			'bannerA': 'Banner A',
		}

class CreateOwnerUserForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')
		widgets = {
		}

class EditExpoOwnerForm(ModelForm):
	class Meta:
		model = Expo
		fields = ('nombre', 'bannerA', 'bannerB', 'video', 'TripticoPage1', 'Calendario' )
		widgets = {
		}
		labels = {
			'nombre': 'Nombre del stand', 'bannerA': 'Banner Hall Izquierdo', 'bannerB': 'Banner Hall Derecho', 'video': 'Video del Hall', 'TripticoPage1': 'Triptico'
		}

class EditStandExpositorForm(ModelForm):
	class Meta:
		model = Stand
		fields = ('banner1', 'banner2', 'banner3', 'banner4', 'banner5', 'banner6', 'banner_horizontal1', 'banner_horizontal2', 'banner_horizontal3', 'logotipo', 'video_bienvenida', 'whatsapp', 'chat', 'webpage', 'flyer_file', 'exhibition_video', 'color1', 'color2')
		widgets = {
		}

class CreateUserForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')
		widgets = {
		}

class EditPlatformUser(ModelForm):
	class Meta:
		OPTIONS = (
	        ("Dueño de expo", "EXO"),
	        ("Dueño de stand", "STO"),
	        ("Visitante", "VIW")
        )
		model = PlatformUser
		fields = ('name', 'user_expo', 'user_type')
		widgets = {
			'user_type': Select(choices=OPTIONS),
		}
		labels={
			'name': 'nombre',
			'user_expo': 'Expos de las que es dueño',
			'user_type': 'Privilegios asignados'
		}

class EditPlatformUser2(ModelForm):
	class Meta:
		model = PlatformUser
		fields = ('user_stand', 'name')
		widgets = {
		}

class EditStandExpoOwnerForm(ModelForm):
	class Meta:
		model = Stand
		fields = ('nombre', 'packageStand', 'standType')
		widgets = {
		}
