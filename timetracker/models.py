# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Recurso(models.Model):

    DESARROLLADOR = 'DE'
    LIDER_PROYECTO = 'LP'

    ESPECIALIDADES = (
        (DESARROLLADOR, 'Desarrollador'),
        (LIDER_PROYECTO, 'Lider de proyecto')
    )

    user = models.OneToOneField(User)
    especialidad = models.CharField(max_length=100, choices=ESPECIALIDADES)

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name


class Proyecto(models.Model):

    EN_PROGRESO = 'EP'
    CANCELADO = 'PA'
    FINALIZADO = 'FI'


    ESTADOS = (
        (EN_PROGRESO, 'En proceso'),
        (CANCELADO, 'Pausado'),
        (FINALIZADO, 'Finalizado'),
    )
    nombre = models.CharField(max_length=60)
    detalle = models.CharField(max_length=5000)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_estimada = models.DateField()
    presupuesto = models.IntegerField()
    estado = models.CharField(max_length=2, choices=ESTADOS, default=EN_PROGRESO)

    def __unicode__(self):
        return self.nombre


class Tarea(models.Model):

    PENDIENTE = 'PE'
    EN_PROGRESO = 'EP'
    RESUELTA = 'FI'
    ANULADA = 'AN'

    ESTADOS = (
        (PENDIENTE, 'Pendiente'),
        (EN_PROGRESO, 'En progreso'),
        (RESUELTA, 'Resuelta'),
        (ANULADA, 'Anulada')
    )

    BAJA = 'BA'
    MEDIA = 'M'
    ALTA = 'A'
    BLOQUEANTE = 'BL'

    PRIORIDADES = (
        (BAJA, 'Baja'),
        (MEDIA, 'Media'),
        (ALTA, 'Alta'),
        (BLOQUEANTE, 'Bloqueante')
    )

    titulo = models.CharField(max_length=60)
    recurso = models.ForeignKey(Recurso, null=True)
    proyecto = models.ForeignKey(Proyecto, null=True)
    detalle = models.CharField(max_length=5000)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estimacion = models.IntegerField()
    horas_trabajadas = models.IntegerField()
    prioridad = models.CharField(max_length=2, choices=PRIORIDADES, null=True)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=PENDIENTE)
