from django import forms
from django.forms import ModelForm, Textarea, TextInput, MultipleChoiceField, Select
from .models import Contact, Expo, Stand
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

class EditStandExpositorForm(ModelForm):
	class Meta:
		model = Stand
		fields = ('logotipo', 'video_bienvenida', 'whatsapp', 'chat', 'webpage', 'flyer_file', 'exhibition_video', 'color1', 'color2')
		widgets = {
		}