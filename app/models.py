from django.db import models

# mi base de datos 


class Empresa(models.Model):
    
    nombre=models.CharField(max_length=150)
    telefono=models.CharField(max_length=10)
    persona_contacto=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}" 

    
    
academicos=[
    ("Basica","Basica"),
    ("Secundaria","Secundaria"),
    ("Tecnica","Tecnica"),
    ("Tecnologia","Tecnologia"),
    ("Ingenieria","Ingenieria"),
    ("Licenciatura","Licenciatura"),
    ("Doctorado","Doctorado"),
]

class DatosUsuario(models.Model):
    # id=models.IntegerField(primary_key=True)
    documento_identidad=models.IntegerField(null=False,blank=False)
    nombres=models.CharField(max_length=50,null=False,blank=False)
    apellidos=models.CharField(max_length=50,null=False,blank=False)
    fecha_nacimiento=models.DateField(null=False,blank=False)
    edad=models.PositiveSmallIntegerField(null=False,blank=False)
    telefono=models.CharField(max_length=10)
    email=models.EmailField(null=True,blank=True)
    informacion_academica=models.CharField(max_length=20,choices=academicos,null=True,blank=True)
    direccion=models.CharField(max_length=100)
    nombre_empresa= models.ForeignKey(Empresa,on_delete=models.SET_NULL, null=True, blank=True)
    cargo=models.CharField(max_length=70)
    nombre_contacto=models.CharField(max_length=50)
    telefono_contacto=models.CharField(max_length=10)
    eps=models.CharField(max_length=30, null=True,blank=True)
    arl=models.CharField(max_length=30, null=True,blank=True)
    pensiones=models.CharField(max_length=30 ,null=True,blank=True)
    fecha_examen_medico=models.DateField(null=True,blank=True)
    curso_altura=models.DateField(null=True,blank=True)
    curso_espacios_confinados=models.DateField(null=True,blank=True)
    imagen=models.ImageField(default='w.jpg')
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
# class Curso(models.Model):
#     usuario=models.ForeignKey(DatosUsuario,on_delete=models.CASCADE,related_name="cursos") 
# #    relacionar las tablas

#     # eps=models.CharField(max_length=30)
#     # arl=models.CharField(max_length=30)
#     # pensiones=models.CharField(max_length=30)
#     fecha_examen_medico=models.DateField(null=False,blank=False)
#     curso_altura=models.DateField(null=True,blank=True)
#     curso_espacios_confinados=models.DateField(null=True,blank=True)
    
#     def __str__(self):
#         return f"Informacion {self.usuario} - Examen médico: {self.fecha_examen_medico}"


