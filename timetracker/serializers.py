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

    id = serializers.IntegerField(read_only=True, required=False)
    titulo = serializers.CharField(max_length=60, required=False)
    proyecto = ProyectoSerializer(required=False)
    detalle = serializers.CharField(max_length=5000, required=False)
    fecha_creacion = serializers.DateTimeField(required=False)
    fecha_inicio = serializers.DateTimeField(required=False)
    fecha_fin = serializers.DateTimeField(required=False)
    estimacion = serializers.IntegerField(required=False)
    horas_trabajadas = serializers.IntegerField(required=False, max_value=24)
    prioridad = serializers.ChoiceField(choices=PRIORIDADES, required=False)
    estado = serializers.ChoiceField(choices=ESTADOS, required=False)

    def create(self, validated_data):
        return Tarea(id=None, **validated_data)

    def update(self, instance, validated_data):
        if not instance.horas_trabajadas:
            instance.horas_trabajadas = validated_data['horas_trabajadas']
        else:
            instance.horas_trabajadas += validated_data['horas_trabajadas']
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


class CargaHorasSerializer(serializers.Serializer):
    horas_trabajadas = serializers.IntegerField()
