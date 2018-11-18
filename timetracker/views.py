# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from . import recursos, tareas
from serializers import RecursoSerializer, TareaSerializer, CargaHorasSerializer


class RecursoViewSet(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = RecursoSerializer

    def list(self, request):
        serializer = RecursoSerializer(
            instance=recursos.values(), many=True
        )
        return Response({'recursos': serializer.data}, template_name='recursos.html')

    def retrieve(self, request, pk):
        serializer = RecursoSerializer(
                instance=recursos[int(pk)]
        )
        tareas = serializer.data.pop('tareas')
        return Response({'recurso': serializer.data, 'tareas': tareas}, template_name='recurso.html')


class TareaDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get_data(self, tarea, recurso):
        tarea_serializer = TareaSerializer(instance=tarea)
        recurso_serializer = RecursoSerializer(recurso)
        carga_horas = CargaHorasSerializer(instance=tarea)
        return {'tarea': tarea_serializer.data, 'recurso': recurso_serializer.data, 'serializer': carga_horas}

    def get(self, request, id_recurso, id_tarea):
        tarea = tareas[int(id_tarea)]
        recurso = recursos[int(id_recurso)]
        return Response(self.get_data(tarea, recurso), template_name='tarea.html')

    def post(self, request, id_recurso, id_tarea):
        try:
            tarea = tareas[int(id_tarea)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        recurso = recursos[int(id_recurso)]
        serializer = TareaSerializer(
            data=request.data, instance=tarea)
        if serializer.is_valid():
            tarea = serializer.save()
            tareas[tarea.id] = tarea
            return Response(self.get_data(tarea, recurso), template_name='tarea.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
