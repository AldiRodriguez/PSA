# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from django.shortcuts import render

from serializers import ProyectoSerializer, TareaSerializer
from models import Proyecto, Tarea


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer