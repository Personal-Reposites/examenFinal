from tarea import Tarea
import csv

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, tarea):
        self.tareas.remove(tarea)

    def modificar_tarea(self, tarea, nuevo_titulo, nueva_descripcion, nuevo_estado, nueva_prioridad):
        tarea.titulo = nuevo_titulo
        tarea.descripcion = nueva_descripcion
        tarea.estado = nuevo_estado
        tarea.prioridad = nueva_prioridad

    def listar_tareas(self):
        return self.tareas

    def exportar_tareas_csv(self, archivo):
        with open(archivo, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Título", "Descripción", "Estado", "Prioridad"])
            for tarea in self.tareas:
                writer.writerow([tarea.titulo, tarea.descripcion, tarea.estado, tarea.prioridad])

    def importar_tareas_csv(self, archivo):
        with open(archivo, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Saltar la cabecera
            self.tareas = [Tarea(t[0], t[1], t[2], t[3]) for t in reader]
