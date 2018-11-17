# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from . import recursos
from serializers import RecursoSerializer


class RecursoViewSet(viewsets.ViewSet):

    serializer_class = RecursoSerializer

    def list(self, request):
        serializer = RecursoSerializer(
            instance=recursos.values(), many=True
        )
        return Response(serializer.data)