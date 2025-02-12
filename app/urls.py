from django.urls import path
from . import views
from . views import registro



urlpatterns = [
    
    path('base/',views.base,name='base'),
    path('',views.principal,name='home'),
    path('lista/',views.lista,name='lista'),
    path('lista/',views.lista_empresa,name='lista'),
    path('registrar_usuario/', views.registrarUsuario, name='registrar_usuario'),
    path('registrar_empresa/', views.registrarEmpresa, name='registrar_empresa'),
    path('usuario/<int:id>/', views.obtener_usuario_y_cursos, name='obtener_usuario_y_cursos'),
    path('registro/',views.registro,name='registro'),
    path('editarUsuario/<int:id>',views.editarUsuario,name='editarUsuario'),
    # path('editar/',views.editar,name='editar'),
    path('eliminar<int:id>/',views.eliminar,name='eliminar'),
    path('empresas<int:id>/',views.filtro_empresa,name='filtro_empresa'),
    path('perfilUsuario/', views.perfilUsuario, name='perfilUsuario'),
    
 
    
]

