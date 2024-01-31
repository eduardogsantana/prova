from django.urls import path, include
from .views import index, register, delete_consulta
from rest_framework import routers
from .api.viewsets import ConsultaViewSet

router = routers.DefaultRouter()
router.register(r'gerenciamento_consultas', ConsultaViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('delete/<int:id>', delete_consulta, name='delete_consulta'),
    path('api_gerenciamento_consulta', include(router.urls))

]
