from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from views import RecursoViewSet, TareaDetailView, get_tarea

router = DefaultRouter()
router.register(r'recursos', RecursoViewSet, basename='recursos')

urlpatterns = [
    url(r'^tareas/(?P<id_recurso>(\d+))/(?P<id_tarea>(\d+))$', TareaDetailView.as_view(), name='tarea'),
    url(r'^tareas/(?P<id_tarea>(\d+))$', get_tarea, name='tarea'),
]
urlpatterns += router.urls
