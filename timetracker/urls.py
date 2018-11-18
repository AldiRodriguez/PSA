from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from views import RecursoViewSet, TareaDetailView

router = DefaultRouter()
router.register(r'recursos', RecursoViewSet, basename='recursos')

urlpatterns = [
    url(r'^tareas/(?P<id_recurso>(\d+))/(?P<id_tarea>(\d+))$', TareaDetailView.as_view(), name='tarea'),
]
urlpatterns += router.urls
