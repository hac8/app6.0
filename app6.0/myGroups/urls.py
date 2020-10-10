from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("grupos", views.groupsMenu, name="groups_home"),
    path("grupos/nuevo/", views.newGroup),
    path("grupos/editar/<str:pk>/", views.updateGroup, name="grupos_editar"),
    path("grupos/eliminar/<str:pk>/", views.deleteGroup, name="grupos_eliminar"),
    path("grupos/nuevo/alumnos/", views.newStudent, name="alumno_nuevo"),
    path("grupos/lista/<str:pk>", views.groupList, name="grupo_lista"),
]