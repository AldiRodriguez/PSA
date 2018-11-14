from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from views import (
    ProyectoViewSet,
    TareaViewSet,
    UserViewSet,
    RecursoViewSet)

router = DefaultRouter()
router.register(r'proyecto', ProyectoViewSet, basename='proyecto')
router.register(r'tarea', TareaViewSet, basename='tarea')
router.register(r'recurso', RecursoViewSet, basename='recurso')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls
