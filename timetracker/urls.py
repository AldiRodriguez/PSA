from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from views import RecursoViewSet, TareaViewSet

router = DefaultRouter()
router.register(r'recursos', RecursoViewSet, basename='recursos')
router.register(r'tareas', TareaViewSet, basename='tareas')

urlpatterns = router.urls
