from django.contrib.auth.models import User

from rest_framework import serializers

from models import Proyecto, Tarea, Recurso


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')


class RecursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recurso
        fields = '__all__'


class ProyectoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Proyecto
        fields = '__all__'


class TareaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tarea
        fields = '__all__'
