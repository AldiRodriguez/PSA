# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from . import recursos, tareas
from serializers import RecursoSerializer, TareaSerializer


class RecursoViewSet(viewsets.ViewSet):

    serializer_class = RecursoSerializer

    def list(self, request):
        serializer = RecursoSerializer(
            instance=recursos.values(), many=True
        )
        return Response(serializer.data)


class TareaViewSet(viewsets.ViewSet):
    serializer_class = TareaSerializer

    def list(self, request):
        serializer = TareaSerializer(
            instance=tareas.values(), many=True
        )
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            tarea = tareas[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = TareaSerializer(
            data=request.data, instance=tarea)
        if serializer.is_valid():
            tarea = serializer.save()
            tareas[tarea.id] = tarea
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
