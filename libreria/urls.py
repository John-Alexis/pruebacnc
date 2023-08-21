from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    
    path('',views.inicio, name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('servicios',views.servicios,name='servicios'),
    path('contactenos',views.contactenos,name='contactenos'),
    path('cliente',views.clientes,name='cliente'),
    path('cliente/crear',views.crearUsuario,name='crear'),
    path('cliente/editar',views.editarUsuario,name='editar'),
    path('eliminar/<int:id>',views.eliminarUsuario,name='eliminar'),
    path('cliente/editar/<int:id>',views.editarUsuario,name='editar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)