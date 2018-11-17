# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Recurso(object):
    fields = ['id', 'nombre', 'apellido', 'tareas', 'especialidad']

    def __init__(self, **kwargs):
        for field in self.fields:
            setattr(self, field, kwargs.get(field, None))


class Proyecto(object):

    fields = ['id',
              'nombre',
              'detalle',
              'fecha_inicio',
              'fecha_fin',
              'fecha_estimada',
              'presupuesto',
              'estado']

    def __init__(self, **kwargs):
        for field in self.fields:
            setattr(self, field, kwargs.get(field, None))


class Tarea(object):
    fields = ['id',
              'titulo',
              'proyecto',
              'detalle',
              'fecha_inicio',
              'fecha_fin',
              'fecha_creacion',
              'estimacion',
              'horas_trabajadas',
              'prioridad',
              'estado']

    def __init__(self, **kwargs):
        for field in self.fields:
            setattr(self, field, kwargs.get(field, None))
