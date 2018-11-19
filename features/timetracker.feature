# Created by arodriguez at 19/11/18
Feature: timetracker
  # Enter feature description here

  Scenario: carga de horas para una tarea
    Given un recurso y una tarea
   	  When hacemos submit de 8 horas
      When obtenemos los datos de la tarea
      Then la tarea queda con 8 horas cargadas
