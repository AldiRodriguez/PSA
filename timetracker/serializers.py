from rest_framework import serializers

from models import Proyecto, Tarea


class ProyectoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Proyecto
        fields = '__all__'


class TareaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tarea
        fields = '__all__'
