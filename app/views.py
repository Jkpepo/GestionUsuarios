from django.shortcuts import render,redirect,get_object_or_404
#debo importar los datos de mis modelos (base de datos)
from .models import DatosUsuario,Empresa
from django.contrib.auth.decorators import login_required #libreria para privatizar solo con registro algunas plantillas
from .forms import CustomUserCreationForm,DatosUsuarioForm,EmpresaForm
from django.contrib.auth import authenticate,login # me permite autenticar  el usuario
from django.contrib.auth.models import User #importar la libreria para el registro de django
from django.contrib import messages
import os
# Create your views here.

def principal (request):
    return render(request,"home.html")

@login_required
def lista(request):
   empresa = Empresa.objects.all()
   busqueda= request.GET.get("buscar")
   if busqueda:
       usuarios=DatosUsuario.objects.filter(nombres__startswith=busqueda)#nombres__contains nombres que contengan alguna letra
       #nombres que inicien es startswith Y istartswith para mayusculas y minusculas
       return render(request,"lista.html",{"usuarios":usuarios})
   else:
        usuarios=DatosUsuario.objects.all()
   return render(request,"lista.html",{"usuarios":usuarios,"empresa":empresa})

def lista_empresa(request):
    
    empresa = Empresa.objects.all()
      
    return render(request,"lista.html",{"empresa":empresa})




def base(request):
  
    return render(request,"base.html") 



@login_required
def perfilUsuario(request):
    user = request.user  # Obtienes el usuario autenticado
    return render(request, "perfilUsuario.html", {"user": user})


def filtro_empresa(request,id):
    empresa=get_object_or_404(Empresa,id=id)
    usuario = DatosUsuario.objects.filter(nombre_empresa=empresa)
    return render(request, "empresas.html", {"usuario": usuario, "empresa":empresa})

@login_required
def obtener_usuario_y_cursos(request,id):
    # Obtén el usuario basado en el ID
    usuario = get_object_or_404(DatosUsuario, id=id)# esto ME REGRESA LO QUE ENCUNETRE POR EL ID
    
    # Obtén las empresas relacionados con el usuario
    empresa = usuario.nombre_empresa
    # curso= usuario.curso_altura
    # Usa el objeto usuario y trae solo los cursos relacionados con el usuario
   
    # Renderiza la plantilla pasando el objeto usuario y las empresas
    return render(request, "usuario_detalle.html", {"usuario": usuario, "empresa":empresa})

@login_required
def registrarUsuario(request):
    if request.method == 'POST':
        form = DatosUsuarioForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el objeto en la base de datos
            return redirect('lista')  # Redirige a una página de éxito o muestra un mensaje
        else:
            return render(request, 'registrar_usuario.html', {'form': form})

    form = DatosUsuarioForm()
    return render(request, 'registrar_usuario.html', {'form': form})

def registrarEmpresa(request):
    if request.method == "POST":
        form=EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
        else:
            return render(request,'registar_empresa.html',{'form':form})
    form = EmpresaForm()
    return render(request, 'registrar_empresa.html', {'form': form})




def registro(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)

        if formulario.is_valid():# si el formulario es valido
          
            # Guarda el usuario en la base de datos
            formulario.save()

            # Mensaje de éxito para el registro
            messages.success(request, "Usuario registrado exitosamente.")
            
            # Redirige a la vista principal (o cualquier otra vista que desees)
            # return redirect('principal')  # Redirige a la vista principal después del registro

        else:
            # Si el formulario no es válido, muestra los errores
            messages.error(request, "Hay un error en el formulario.")
            print(formulario.errors)  # Esto es útil para depuración
    else:
        formulario = CustomUserCreationForm()  # Crea un formulario vacío para el GET
        
    return render(request, "registration/registro.html", {'form': formulario})
    

       
            
    #         if password1 != password2:
    #             messages.error(request, "Las contraseñas no coinciden.")
    #             return render(request, "registration/registro.html", {'form': form})

    #         if User.objects.filter(username=username).exists():
    #             messages.error(request, "El nombre de usuario ya está en uso.")
    #             return render(request, "registration/registro.html", {'form': form})


# editar basicamente lo que hago es una funcion que me toma el id mediente el get
#despues le envio a la plantilla editarUSuario y en esa plantilla la accion del form
#le pongo/editar/ mi otra funcion y me toma el id
def editarUsuario(request,id):
    usuario=DatosUsuario.objects.get(id=id)
    
    if request.method == 'POST':
        formulario= DatosUsuarioForm(request.POST,request.FILES,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.info(request, "Registro actualizado exitosamente.")
            # return redirect('lista')
    else:
        formulario = DatosUsuarioForm(instance=usuario)
    return render(request,"editarUsuario.html",{"formulario":formulario})

    

def eliminar(request,id):
    usuario=DatosUsuario.objects.get(id=id)
    # Elimina la imagen del sistema de archivos
    if usuario.imagen:
        if os.path.isfile(usuario.imagen.path):
            os.remove(usuario.imagen.path)
    
    usuario.delete()
    return redirect("lista")
    

    