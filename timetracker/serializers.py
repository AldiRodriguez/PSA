from django.contrib.auth.models import User

from rest_framework import serializers

from models import Proyecto, Tarea, Recurso


class ProyectoSerializer(serializers.Serializer):
    ESTADOS = ['En proceso', 'Pausado', 'Finalizado']

    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=60)
    detalle = serializers.CharField(max_length=5000)
    fecha_inicio = serializers.DateTimeField()
    fecha_fin = serializers.DateTimeField()
    fecha_estimada = serializers.DateField()
    presupuesto = serializers.IntegerField()
    estado = serializers.ChoiceField(choices=ESTADOS, default='En_proceso')

    def create(self, validated_data):
        return Proyecto(**validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class TareaSerializer(serializers.Serializer):

    ESTADOS = ['Anulada', 'Resuelta', 'En progreso', 'Pendiente']
    PRIORIDADES = ['Bloqueante', 'Alta', 'Media', 'Baja']

    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(max_length=60)
    proyecto = ProyectoSerializer()
    detalle = serializers.CharField(max_length=5000)
    fecha_creacion = serializers.DateTimeField()
    fecha_inicio = serializers.DateTimeField()
    fecha_fin = serializers.DateTimeField()
    estimacion = serializers.IntegerField()
    horas_trabajadas = serializers.IntegerField()
    prioridad = serializers.ChoiceField(choices=PRIORIDADES)
    estado = serializers.ChoiceField(choices=ESTADOS)

    def create(self, validated_data):
        return Tarea(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class RecursoSerializer(serializers.Serializer):
    ESPECIALIDADES = ('Desarrollador', 'Lider de Proyecto')

    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=200)
    apellido = serializers.CharField(max_length=200)
    tareas = TareaSerializer(many=True)
    especialidad = serializers.ChoiceField(choices=ESPECIALIDADES)

    def create(self, validated_data):
        return Recurso(**validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
