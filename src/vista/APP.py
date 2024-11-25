import tkinter as tk
from tkinter import ttk

class GestionContrasenasWindow:
    def __init__(self, usuario_id):
        self.eliminar_contrasena = None
        self.editar_contrasena = None
        self.agregar_contrasena = None
        self.usuario_id = usuario_id  # Recibe el id del usuario

        # Configurar ventana principal
        self.root = tk.Tk()
        self.root.title("Gestión de Contraseñas")
        self.root.geometry("800x400")

        # Tabla de contraseñas
        self.tree = ttk.Treeview(self.root, columns=(
            "ID", "Servicio", "Usuario", "Contraseña Encriptada", "Fecha de Creación", "Última Modificación", "Nota"),
            show="headings")

        # Definir encabezados de las columnas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Servicio", text="Servicio")
        self.tree.heading("Usuario", text="Usuario")
        self.tree.heading("Contraseña Encriptada", text="Contraseña Encriptada")
        self.tree.heading("Fecha de Creación", text="Fecha de Creación")
        self.tree.heading("Última Modificación", text="Última Modificación")
        self.tree.heading("Nota", text="Nota")

        # Ajustar el ancho de las columnas
        self.tree.column("ID", width=50)
        self.tree.column("Servicio", width=150)
        self.tree.column("Usuario", width=150)
        self.tree.column("Contraseña Encriptada", width=150)
        self.tree.column("Fecha de Creación", width=150)
        self.tree.column("Última Modificación", width=150)
        self.tree.column("Nota", width=200)

        # Mostrar la tabla
        self.tree.pack(fill="both", expand=True)

        # Botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack()

        tk.Button(frame_botones, text="Agregar").pack(side="left", padx=10)
        tk.Button(frame_botones, text="Editar").pack(side="left", padx=10)
        tk.Button(frame_botones, text="Eliminar").pack(side="left", padx=10)

    def run(self):
        """Método para iniciar el bucle principal."""
        self.root.mainloop()


if __name__ == "__main__":
    app = GestionContrasenasWindow(usuario_id=1)
    app.run()
