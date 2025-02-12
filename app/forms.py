
import hashlib # esta libreria es para hashear el codigo de verificacion para el registro
from django import forms
from . models import DatosUsuario,Empresa
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    codigo = forms.CharField(max_length=10, required=True, help_text="Introduce el código de registro.")#extendiendo la clase para agregar el campo codigo a mi formulario de registro
    
    CODIGO_REGISTRO_HASH = "6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090"#codigo de registro abc123 encriptado
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','codigo']  # Asegúrate de que estos sean los campos correctos
        
    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')#limpia los campos el cleaned data para que no quede el codigo 
        
        # Realizamos el hash del código ingresado
        hashed_codigo_ingresado = hashlib.sha256(codigo.encode('utf-8')).hexdigest()
        
        # Comparamos el hash del código ingresado con el hash predefinido
        if hashed_codigo_ingresado != self.CODIGO_REGISTRO_HASH:
            raise ValidationError("Código de registro incorrecto.")
        
        return codigo
    
    
    from .models import DatosUsuario

class DatosUsuarioForm(forms.ModelForm):
    class Meta:
        model = DatosUsuario
        fields = "__all__"
        
        widgets = {
            'fecha_nacimiento':forms.TextInput(attrs={'type':'date','class': 'form-control', 'placeholder': 'dd/mm/yyyy'}),
            'fecha_examen_medico':forms.TextInput(attrs={'type':'date','class': 'form-control', 'placeholder': 'dd/mm/yyyy'}),
            'curso_altura':forms.TextInput(attrs={'type':'date','class': 'form-control', 'placeholder': 'dd/mm/yyyy'}),
            'curso_espacios_confinados':forms.TextInput(attrs={'type':'date','class': 'form-control', 'placeholder': 'dd/mm/yyyy'}),
            # 'fecha_examen_medico': forms.DateInput(attrs={ 'class': 'form-control','placeholder': 'dia/mes/año'}),
            # 'curso_altura': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            # 'curso_espacios_confinados': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            # 'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Documento identidad'}),
        #     'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
        #     'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            #  'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
        #     'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        #     'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
        #     'cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo'}),
        #     'nombre_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de contacto'}),
        #     'telefono_contacto': forms.TextInput(attrs={'id':'namer','class': 'form-control ', 'placeholder': 'Teléfono de contacto'}),
        #     'eps': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'EPS'}),
        #     'arl': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ARL'}),
        #     'pensiones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fondo de pensiones'}),
         }
class EmpresaForm(forms.ModelForm):
    class Meta:
        model=Empresa
        fields= "__all__"
        
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Solo los campos que deseas permitir modificar