class Tarea:
    def __init__(self, titulo, descripcion, estado="Pendiente", prioridad="Normal"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado  # "Pendiente" o "Completada"
        self.prioridad = prioridad  # "Baja", "Normal", "Alta"

    def __str__(self):
        return f"{self.titulo} - {self.estado} - {self.prioridad}"
