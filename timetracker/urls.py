from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from views import ProyectoViewSet, TareaViewSet

router = DefaultRouter()
router.register(r'proyecto', ProyectoViewSet, basename='proyecto')
router.register(r'tarea', TareaViewSet, basename='tarea')
urlpatterns = router.urls
