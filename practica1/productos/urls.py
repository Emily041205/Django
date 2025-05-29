
from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_productos, name='listar_productos'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('completar/<int:producto_id>/', views.marcar_completado, name='marcar_completado'),
]


