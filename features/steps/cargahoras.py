from behave import *
from datetime import datetime

from timetracker import recursos
import requests

use_step_matcher("re")


@given("un recurso y una tarea")
def step_impl(context):

    context.recurso = recursos[1]
    context.tarea = context.recurso.tareas[0]


@when("hacemos submit de 8 horas")
def step_impl(context):

    url = 'http://localhost:8000/tareas/{0}/{1}'.format(context.recurso.id, context.tarea.id)
    requests.post(url, data={'horas_trabajadas': 8})


@when("obtenemos los datos de la tarea")
def step_impl(context):

    url = 'http://localhost:8000/tareas/{0}'.format(context.tarea.id)
    response = requests.get(url)
    context.response = response.json()


@then("la tarea queda con 8 horas cargadas")
def step_impl(context):

    assert (context.response['horas_trabajadas'] == 8)


@when("hacemos submit de -1 horas")
def step_impl(context):
    url = 'http://localhost:8000/tareas/{0}/{1}'.format(context.recurso.id, context.tarea.id)
    context.response = requests.post(url, data={'horas_trabajadas': -1})


@then("el servidor tira error")
def step_impl(context):

    assert (context.response.status_code == 400)


@when("hacemos submit de 9 horas")
def step_impl(context):
    url = 'http://localhost:8000/tareas/{0}/{1}'.format(context.recurso.id, context.tarea.id)
    context.response = requests.post(url, data={'horas_trabajadas': 25})