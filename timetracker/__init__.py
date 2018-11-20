from datetime import datetime
from models import Proyecto, Tarea, Recurso


proyectos = {
    1: Proyecto(id=1,
                nombre='PSA',
                detalle='App de venta de productos',
                fecha_inicio=datetime.now(),
                presupuesto=400000,
                estado='En proceso'),
    2: Proyecto(id=2,
                nombre='Nike',
                detalle='Control de stock ',
                fecha_inicio=datetime.now(),
                presupuesto=900000,
                estado='En proceso'),
}

tareas = {1: Tarea(id=1,
                   titulo='Tarea uno',
                   proyecto=proyectos[1],
                   detalle='Tarea uno',
                   fecha_creacion=datetime.now(),
                   estimacion=8,
                   prioridad='Baja',
                   estado='Pendiente',
                   horas_trabajadas=0),
          2: Tarea(id=2,
                   titulo='Tarea dos',
                   proyecto=proyectos[1],
                   detalle='tarea dos',
                   fecha_creacion=datetime.now(),
                   estimacion=13,
                   prioridad='Media',
                   estado='En progreso',
                   horas_trabajadas=0),
          3: Tarea(id=3,
                   titulo='Tarea tres',
                   proyecto=proyectos[2],
                   detalle='tarea tres',
                   fecha_creacion=datetime.now(),
                   estimacion=40,
                   prioridad='Alta',
                   estado='Pendiente',
                   horas_trabajadas=0)}
recursos = {
    1: Recurso(
        id=1,
        nombre='Felipe',
        apellido='Codeo',
        especialidad='Desarrollador',
        tareas=tareas.values()
    )
}