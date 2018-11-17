from datetime import datetime
from models import Proyecto, Tarea, Recurso


proyectos = {
    1: Proyecto(nombre='PSA',
                detalle='App de venta de productos',
                fecha_inicio=datetime.now(),
                presupuesto=400000,
                estado='En proceso'),
    2: Proyecto(nombre='Nike',
                detalle='Control de stock ',
                fecha_inicio=datetime.now(),
                presupuesto=900000,
                estado='En proceso'),
}

tareas = {1: Tarea(titulo='Tarea uno',
                   proyecto=proyectos[1],
                   detalle='Tarea uno',
                   fecha_creacion=datetime.now(),
                   estimacion=8,
                   prioridad='Baja',
                   estado='Pendiente'),
          2: Tarea(titulo='Tarea dos',
                   proyecto=proyectos[1],
                   detalle='tarea dos',
                   fecha_creacion=datetime.now(),
                   estimacion=13,
                   prioridad='Media',
                   estado='En progreso'),
          3: Tarea(titulo='Tarea tres',
                   proyecto=proyectos[2],
                   detalle='tarea tres',
                   fecha_creacion=datetime.now(),
                   estimacion=40,
                   prioridad='Alta',
                   estado='Pendiente')}
recursos = {
    1: Recurso(
        nombre='Aldana',
        apellido='Rodriguez',
        especialidad='Desarrollador',
        tareas=tareas.values()
    )
}