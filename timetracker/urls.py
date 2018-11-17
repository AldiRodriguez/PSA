from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from views import RecursoViewSet

router = DefaultRouter()
router.register(r'recursos', RecursoViewSet, basename='recursos')

urlpatterns = router.urls
