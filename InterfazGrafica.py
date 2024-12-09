import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from gestor_tareas import GestorTareas
from tarea import Tarea

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.gestor = GestorTareas()

        #style boton
        self.button_style = {"width": 20, "height": 2, "bg": "#4CAF50", "fg": "white", "font": ("Arial", 12)}

        # Crear encabezado de la lista
        self.label_encabezado = tk.Label(root, text="Título - Estado - Prioridad", font=("Arial", 10, "bold"))
        self.label_encabezado.pack()

        # Crear lista de tareas
        self.lista_tareas = tk.Listbox(root, height=10, width=50)
        self.lista_tareas.pack(pady=20)

        # Botones
        self.btn_agregar = tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea, **self.button_style)
        self.btn_agregar.pack(pady=5)

        self.btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea, **self.button_style)
        self.btn_eliminar.pack(pady=5)

        self.btn_modificar = tk.Button(root, text="Modificar Tarea", command=self.modificar_tarea, **self.button_style)
        self.btn_modificar.pack(pady=5)

        self.btn_ver_descripcion = tk.Button(root, text="Ver Descripción", command=self.ver_descripcion, **self.button_style)
        self.btn_ver_descripcion.pack(pady=5)

        self.btn_exportar_csv = tk.Button(root, text="Exportar a CSV", command=self.exportar_csv, **self.button_style)
        self.btn_exportar_csv.pack(pady=5)

        self.btn_importar_csv = tk.Button(root, text="Importar desde CSV", command=self.importar_csv, **self.button_style)
        self.btn_importar_csv.pack(pady=5)

    #metodos

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.gestor.listar_tareas():
            self.lista_tareas.insert(tk.END, str(tarea))

    def agregar_tarea(self):
        titulo = simpledialog.askstring("Título", "Ingrese el título de la tarea:")
        descripcion = simpledialog.askstring("Descripción", "Ingrese la descripción de la tarea:")
        estado = simpledialog.askstring("Estado", "Ingrese el estado de la tarea (Pendiente o Completada):", initialvalue="Pendiente")
        prioridad = simpledialog.askstring("Prioridad", "Ingrese la prioridad de la tarea (Baja, Normal, Alta):", initialvalue="Normal")

        if titulo and descripcion and estado and prioridad:
            tarea = Tarea(titulo, descripcion, estado, prioridad)
            self.gestor.agregar_tarea(tarea)
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea_seleccionada = self.gestor.listar_tareas()[seleccion[0]]
            self.gestor.eliminar_tarea(tarea_seleccionada)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Selección", "Seleccione una tarea para eliminar.")

    def modificar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea_seleccionada = self.gestor.listar_tareas()[seleccion[0]]
            nuevo_titulo = simpledialog.askstring("Nuevo Título", "Ingrese el nuevo título de la tarea:", initialvalue=tarea_seleccionada.titulo)
            nueva_descripcion = simpledialog.askstring("Nueva Descripción", "Ingrese la nueva descripción de la tarea:", initialvalue=tarea_seleccionada.descripcion)
            nuevo_estado = simpledialog.askstring("Nuevo Estado", "Ingrese el nuevo estado de la tarea:", initialvalue=tarea_seleccionada.estado)
            nueva_prioridad = simpledialog.askstring("Nueva Prioridad", "Ingrese la nueva prioridad de la tarea:", initialvalue=tarea_seleccionada.prioridad)

            self.gestor.modificar_tarea(tarea_seleccionada, nuevo_titulo, nueva_descripcion, nuevo_estado, nueva_prioridad)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Selección", "Seleccione una tarea para modificar.")

    def ver_descripcion(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea_seleccionada = self.gestor.listar_tareas()[seleccion[0]]
            messagebox.showinfo("Descripción", f"Descripción de '{tarea_seleccionada.titulo}':\n\n{tarea_seleccionada.descripcion}")
        else:
            messagebox.showwarning("Selección", "Seleccione una tarea para ver su descripción.")

    def exportar_csv(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if archivo:
            self.gestor.exportar_tareas_csv(archivo)

    def importar_csv(self):
        archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if archivo:
            self.gestor.importar_tareas_csv(archivo)
            self.actualizar_lista()


root = tk.Tk()
app = Aplicacion(root)
root.mainloop()
