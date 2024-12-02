import tkinter as tk
from tkinter import messagebox, ttk
from sqlalchemy.orm import sessionmaker
from src.modelo.modelo import engine, Etiqueta, Usuario
from src.logica.CRUD import UsuarioCRUD, Contraseniacrud, SesionCRUD

#from datetime import datetime
import random
import string

# Configurar sesión de SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()
usuario_crud = UsuarioCRUD(session)
contrasenia_crud = Contraseniacrud(session)
cerrar_sesion = SesionCRUD(session)

def generar_contrasena(longitud=12):
    """Genera una contraseña aleatoria."""
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return ''.join(random.choice(caracteres) for _ in range(longitud))

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("700x700")  # Tamaño más grande
        self.root.resizable(False, False)
        self.root.configure(bg="#1d1f27")  # Fondo oscuro

        # Estilo para la fuente
        font_style = ("Segoe UI", 14)

        # Encabezado
        self.header = tk.Label(
            root,
            text="Bienvenido",
            font=("Segoe UI", 32, "bold"),
            fg="#00d4b5",  # Color futurista
            bg="#1d1f27",
            pady=20
        )
        self.header.pack(pady=20)

        # Marco para el formulario
        self.frame_form = tk.Frame(root, bg="#2b2f3d", bd=5, relief="solid", padx=30, pady=30)
        self.frame_form.pack(pady=20, padx=30, fill="both", expand=True)
        self.frame_form.config(bg="#2b2f3d")

        # Etiquetas y campos de entrada
        self.label_email = tk.Label(
            self.frame_form,
            text="Correo Electrónico:",
            font=font_style,
            fg="#ffffff",
            bg="#2b2f3d"
        )
        self.label_email.pack(pady=10, anchor="w")
        self.entry_email = ttk.Entry(self.frame_form, width=40, font=("Segoe UI", 12))
        self.entry_email.pack(pady=10, ipadx=5, ipady=5)

        self.label_password = tk.Label(
            self.frame_form,
            text="Contraseña:",
            font=font_style,
            fg="#ffffff",
            bg="#2b2f3d"
        )
        self.label_password.pack(pady=10, anchor="w")
        self.entry_password = ttk.Entry(self.frame_form, width=40, font=("Segoe UI", 12), show="*")
        self.entry_password.pack(pady=10, ipadx=5, ipady=5)

        # Botones con estilo futurista
        style = ttk.Style()
        style.configure("futuristic.TButton",
                        background="#00d4b5",
                        foreground="#1d1f27",
                        font=("Segoe UI", 12, "bold"),
                        relief="flat",
                        padding=10)
        style.map("futuristic.TButton",
                  background=[("active", "#009e8b"), ("disabled", "#444444")])

        self.button_login = ttk.Button(
            self.frame_form,
            text="Iniciar Sesión",
            command=self.login,
            style="futuristic.TButton"
        )
        self.button_login.pack(pady=15, fill="x", padx=20)

        self.button_register = ttk.Button(
            self.frame_form,
            text="Crear Usuario",
            command=self.open_register_window,
            style="futuristic.TButton"
        )
        self.button_register.pack(pady=10, fill="x", padx=20)

        # Pie de página
        self.footer = tk.Label(
            root,
            text="© 2024 - PassKeeper. All rights reserved.",
            font=("Segoe UI", 10),
            bg="#1d1f27",
            fg="#888888",
        )
        self.footer.pack(pady=20)

    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        if not email or not password:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        try:
            sesion = usuario_crud.iniciar_sesion(email, password)
            if sesion:
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
                self.root.destroy()  # Cierra la ventana de login
                GestionContrasenasWindow(sesion.id_usuario)  # Pasa el id_usuario al abrir la ventana de contraseñas
            else:
                messagebox.showerror("Error", "Correo o contraseña incorrectos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

    def open_register_window(self):
        RegisterWindow(self.root)

class RegisterWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Registrar Usuario")
        self.window.geometry("600x850")  # Tamaño más grande
        self.window.resizable(False, False)
        self.window.configure(bg="#1d1f27")  # Fondo oscuro

        # Estilo para la fuente
        font_style = ("Segoe UI", 14)

        # Encabezado
        self.label_title = tk.Label(
            self.window,
            text="Registro de Usuario",
            font=("Segoe UI", 32, "bold"),
            fg="#00d4b5",  # Color futurista
            bg="#1d1f27",
            pady=20
        )
        self.label_title.pack(pady=20)

        # Marco del formulario
        self.form_frame = tk.Frame(self.window, bg="#2b2f3d", bd=5, relief="solid", padx=30, pady=30)
        self.form_frame.pack(padx=30, pady=20, fill="both", expand=True)
        self.form_frame.config(bg="#2b2f3d")

        # Campo: Nombre de Usuario
        self.label_username = tk.Label(
            self.form_frame,
            text="Nombre de Usuario:",
            font=font_style,
            fg="#ffffff",
            bg="#2b2f3d"
        )
        self.label_username.pack(pady=10, anchor="w")
        self.entry_username = ttk.Entry(self.form_frame, width=40, font=("Segoe UI", 12))
        self.entry_username.pack(pady=10, ipadx=5, ipady=5)

        # Campo: Correo Electrónico
        self.label_email = tk.Label(
            self.form_frame,
            text="Correo Electrónico:",
            font=font_style,
            fg="#ffffff",
            bg="#2b2f3d"
        )
        self.label_email.pack(pady=10, anchor="w")
        self.entry_email = ttk.Entry(self.form_frame, width=40, font=("Segoe UI", 12))
        self.entry_email.pack(pady=10, ipadx=5, ipady=5)

        # Campo: Contraseña
        self.label_password = tk.Label(
            self.form_frame,
            text="Contraseña:",
            font=font_style,
            fg="#ffffff",
            bg="#2b2f3d"
        )
        self.label_password.pack(pady=10, anchor="w")
        self.entry_password = ttk.Entry(self.form_frame, width=40, font=("Segoe UI", 12), show="*")
        self.entry_password.pack(pady=10, ipadx=5, ipady=5)

        # Botón: Generar Contraseña
        self.button_generate_password = ttk.Button(
            self.form_frame,
            text="Generar Contraseña",
            command=self.generate_password,
            style="futuristic.TButton"
        )
        self.button_generate_password.pack(pady=10, padx=10)

        # Campo: Rol
        self.label_rol = tk.Label(
            self.form_frame,
            text="Rol (admin, usuario):",
            font=font_style,
            fg="#ffffff",
            bg="#2b2f3d"
        )
        self.label_rol.pack(pady=10, anchor="w")
        self.entry_rol = ttk.Entry(self.form_frame, width=40, font=("Segoe UI", 12))
        self.entry_rol.pack(pady=10, ipadx=5, ipady=5)

        # Botón: Registrar
        self.button_register = ttk.Button(
            self.form_frame,
            text="Registrar",
            command=self.register_user,
            style="futuristic.TButton"
        )
        self.button_register.pack(pady=20, padx=10)

        # Estilo para los botones
        style = ttk.Style()
        style.configure("futuristic.TButton",
                        background="#00d4b5",
                        foreground="#1d1f27",
                        font=("Segoe UI", 12, "bold"),
                        relief="flat",
                        padding=10)
        style.map("futuristic.TButton",
                  background=[("active", "#009e8b"), ("disabled", "#444444")])

    def generate_password(self):
        """Genera una contraseña aleatoria y la coloca en el campo de entrada."""
        nueva_contrasena = generar_contrasena()
        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(0, nueva_contrasena)
        messagebox.showinfo("Contraseña Generada", f"Contraseña: {nueva_contrasena}")

    def register_user(self):
        nombre_usuario = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        rol = self.entry_rol.get()

        if not nombre_usuario or not email or not password or not rol:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        try:
            usuario_crud.create_usuario(nombre_usuario, email, password, rol)
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el usuario: {e}")

class GestionContrasenasWindow:
    def __init__(self, usuario_id):
        self.session = session
        self.SesionCRUD = SesionCRUD(session)
        self.Contraseniacrud = Contraseniacrud(session)
        self.usuario_id = usuario_id  # Recibe el id del usuario
        self.root = tk.Tk()
        self.root.title("Gestión de Contraseñas")
        self.root.geometry("1200x400")

        # Obtener el usuario desde la base de datos
        self.usuario = self.session.query(Usuario).filter_by(id_usuario=usuario_id).first()

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

        # Verificar si el usuario es admin
        if self.usuario.rol == "admin":
            # Si el usuario es admin, habilitar el botón de "Ver Usuarios"
            self.boton_ver_usuarios = tk.Button(frame_botones, text="Ver Usuarios", command=self.mostrar_usuarios)
            self.boton_ver_usuarios.pack(side="left", padx=10)
        else:
            # Si no es admin, deshabilitar el botón
            self.boton_ver_usuarios = tk.Button(frame_botones, text="Ver Usuarios", state="disabled")
            self.boton_ver_usuarios.pack(side="left", padx=10)

        tk.Button(frame_botones, text="Agregar", command=self.agregar_contrasena).pack(side="left", padx=10)
        tk.Button(frame_botones, text="Editar", command=self.editar_contrasena).pack(side="left", padx=10)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_contrasena).pack(side="left", padx=10)
        tk.Button(frame_botones, text="Cerrar sesión", command=self.cerrar_sesion).pack(side="left", padx=10)

        # Cargar contraseñas
        self.cargar_contrasenas()

        self.root.mainloop()

    def mostrar_usuarios(self):
        """Muestra una ventana con la lista de usuarios."""
        # Crear una nueva ventana para mostrar los usuarios
        ventana_usuarios = tk.Toplevel(self.root)
        ventana_usuarios.title("Usuarios Registrados")
        ventana_usuarios.geometry("600x300")

        # Crear una tabla para mostrar los usuarios
        tree_usuarios = ttk.Treeview(ventana_usuarios, columns=("ID", "Nombre de Usuario", "Rol"), show="headings")
        tree_usuarios.heading("ID", text="ID")
        tree_usuarios.heading("Nombre de Usuario", text="Nombre de Usuario")
        tree_usuarios.heading("Rol", text="Rol")

        # Ajustar el ancho de las columnas
        tree_usuarios.column("ID", width=50)
        tree_usuarios.column("Nombre de Usuario", width=200)
        tree_usuarios.column("Rol", width=100)

        # Cargar los usuarios desde la base de datos
        usuarios = self.session.query(Usuario).all()

        # Insertar los datos de los usuarios en la tabla
        for usuario in usuarios:
            tree_usuarios.insert("", "end", values=(usuario.id_usuario, usuario.nombre_usuario, usuario.rol))

        # Mostrar la tabla
        tree_usuarios.pack(fill="both", expand=True)

    def cerrar_sesion(self):
        """Cerrar la sesión desde la interfaz gráfica."""
        respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea cerrar sesión?")
        if respuesta:
            try:
                # Llama al método de CRUD para cerrar la sesión en la base de datos
                self.SesionCRUD.cerrar_sesion(self.usuario_id)
                messagebox.showinfo("Éxito", "Sesión cerrada correctamente.")
                self.root.destroy()  # Cierra la ventana de la aplicación
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def cargar_contrasenas(self):
        """Carga las contraseñas del usuario desde la base de datos"""
        # Limpiar la tabla antes de cargar datos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obtener contraseñas de la base de datos
        contrasenas = contrasenia_crud.obtener_contrasenias_usuario(self.usuario_id)

        # Insertar los datos en la tabla
        for contrasenia in contrasenas:
            self.tree.insert("", "end", values=(
                contrasenia.id_contrasenia,
                contrasenia.servicio,
                contrasenia.nombre_usuario_servicio,
                contrasenia.contrasenia_encriptada,  # Columna de Contraseña Encriptada
                contrasenia.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S") if contrasenia.fecha_creacion else "",
                # Fecha de creación
                contrasenia.ultima_modificacion.strftime(
                    "%Y-%m-%d %H:%M:%S") if contrasenia.ultima_modificacion else "",  # Última modificación
                contrasenia.nota or ""  # Nota (si no hay nota, colocar vacío)
            ))


    def agregar_contrasena(self):
        def guardar_contrasena():
            servicio = entry_servicio.get().strip()
            nombre_usuario_servicio = entry_usuario.get().strip()
            contrasenia = entry_contrasenia.get().strip()
            nota = text_nota.get("1.0", tk.END).strip()

            if not servicio or not nombre_usuario_servicio or not contrasenia:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos obligatorios.")
                return

            # Obtener las etiquetas seleccionadas
            etiquetas_seleccionadas = combo_etiquetas.get().strip()
            if etiquetas_seleccionadas:
                etiquetas_lista = etiquetas_seleccionadas.split(",")  # Separar si son múltiples etiquetas
            else:
                etiquetas_lista = []

            try:
                # Crear la nueva contraseña en la base de datos
                contrasenia_obj = contrasenia_crud.create_contrasenia(
                    id_usuario=self.usuario_id,
                    servicio=servicio,
                    nombre_usuario_servicio=nombre_usuario_servicio,
                    contrasenia_encriptada=contrasenia,  # Aquí deberías encriptar la contraseña
                    nota=nota
                )

                # Asociar las etiquetas seleccionadas a la nueva contraseña
                for etiqueta in etiquetas_lista:
                    etiqueta_obj = self.session.query(Etiqueta).filter_by(nombre=etiqueta).first()
                    if etiqueta_obj:
                        contrasenia_obj.etiquetas.append(etiqueta_obj)

                self.session.commit()

                messagebox.showinfo("Éxito", "Contraseña agregada correctamente.")
                self.cargar_contrasenas()
                ventana_agregar.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar la contraseña: {e}")

        # Crear una nueva ventana para añadir una contraseña
        ventana_agregar = tk.Toplevel(self.root)
        ventana_agregar.title("Agregar Contraseña")
        ventana_agregar.geometry("400x500")

        # Campos de entrada
        tk.Label(ventana_agregar, text="Servicio:").pack(pady=5)
        entry_servicio = tk.Entry(ventana_agregar, width=30)
        entry_servicio.pack(pady=5)

        tk.Label(ventana_agregar, text="Usuario del Servicio:").pack(pady=5)
        entry_usuario = tk.Entry(ventana_agregar, width=30)
        entry_usuario.pack(pady=5)

        tk.Label(ventana_agregar, text="Contraseña:").pack(pady=5)
        entry_contrasenia = tk.Entry(ventana_agregar, width=30, show="*")
        entry_contrasenia.pack(pady=5)

        tk.Label(ventana_agregar, text="Nota (opcional):").pack(pady=5)
        text_nota = tk.Text(ventana_agregar, height=5, width=40)
        text_nota.pack(pady=5)

        # ComboBox para seleccionar etiquetas
        tk.Label(ventana_agregar, text="Etiquetas:").pack(pady=5)
        combo_etiquetas = ttk.Combobox(ventana_agregar, width=30)
        etiquetas = self.session.query(Etiqueta).all()  # Cargar etiquetas desde la base de datos
        combo_etiquetas['values'] = [etiqueta.nombre for etiqueta in etiquetas]  # Mostrar nombres de etiquetas
        combo_etiquetas.pack(pady=5)

        # Botón para guardar
        tk.Button(ventana_agregar, text="Guardar", command=guardar_contrasena).pack(pady=10)

    def editar_contrasena(self):
        # Verificar si hay una contraseña seleccionada
        seleccion = self.tree.focus()  # Obtener la selección en la tabla
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una contraseña para editar.")
            return

        # Obtener los datos de la contraseña seleccionada
        item_seleccionado = self.tree.item(seleccion)
        contrasena_id = item_seleccionado["values"][0]  # Suponiendo que el ID es la primera columna
        servicio_actual = item_seleccionado["values"][1]  # Servicio actual
        usuario_actual = item_seleccionado["values"][2]  # Usuario del servicio actual
        contrasena_actual = item_seleccionado["values"][3]  # Contraseña (encriptada o no)
        nota_actual = item_seleccionado["values"][6]  # Nota actual

        # Crear una nueva ventana para editar la contraseña
        ventana_editar = tk.Toplevel(self.root)
        ventana_editar.title("Editar Contraseña")
        ventana_editar.geometry("400x400")

        # Función para guardar los cambios
        def guardar_contrasena():
            # Obtener los datos ingresados por el usuario
            servicio = entry_servicio.get().strip()
            nombre_usuario_servicio = entry_usuario.get().strip()
            contrasenia = entry_contrasenia.get().strip()  # Aquí obtienes la contraseña nueva
            nota = text_nota.get("1.0", tk.END).strip()

            if not servicio or not nombre_usuario_servicio or not contrasenia:
                messagebox.showerror("Error", "Por favor, complete todos los campos obligatorios.")
                return

            try:
                # Llamar al método editar_contrasenia en CRUD
                self.Contraseniacrud.editar_contrasena(
                    contrasena_id, contrasenia_encriptada=contrasenia, nota=nota,
                    servicio=servicio, usuario=nombre_usuario_servicio
                )
                messagebox.showinfo("Éxito", "La contraseña ha sido editada correctamente.")
                self.cargar_contrasenas()  # Refrescar la tabla después de editar
                ventana_editar.destroy()  # Cerrar la ventana de edición
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo editar la contraseña: {e}")

        # Campos de entrada para editar la contraseña
        tk.Label(ventana_editar, text="Servicio:").pack(pady=5)
        entry_servicio = tk.Entry(ventana_editar, width=30)
        entry_servicio.insert(0, servicio_actual)  # Insertar el valor actual
        entry_servicio.pack(pady=5)

        tk.Label(ventana_editar, text="Usuario del Servicio:").pack(pady=5)
        entry_usuario = tk.Entry(ventana_editar, width=30)
        entry_usuario.insert(0, usuario_actual)  # Insertar el valor actual
        entry_usuario.pack(pady=5)

        tk.Label(ventana_editar, text="Contraseña:").pack(pady=5)
        entry_contrasenia = tk.Entry(ventana_editar, width=30, show="*")
        entry_contrasenia.insert(0, contrasena_actual)  # Inserta la contraseña actual (encriptada o no)
        entry_contrasenia.pack(pady=5)

        tk.Label(ventana_editar, text="Nota (opcional):").pack(pady=5)
        text_nota = tk.Text(ventana_editar, height=5, width=40)
        text_nota.insert(tk.END, nota_actual)  # Insertar la nota actual
        text_nota.pack(pady=5)

        # Botón para guardar
        tk.Button(ventana_editar, text="Guardar", command=guardar_contrasena).pack(pady=10)


    def eliminar_contrasena(self):
        try:
            # Verificar si hay una contraseña seleccionada
            seleccion = self.tree.focus()  # Obtener la selección en la tabla
            if not seleccion:
                messagebox.showwarning("Advertencia", "Por favor, seleccione una contraseña para eliminar.")
                return

            # Obtener datos de la contraseña seleccionada
            item_seleccionado = self.tree.item(seleccion)
            contrasena_id = item_seleccionado["values"][0]  # Suponiendo que el ID es la primera columna

            # Confirmación
            confirmacion = messagebox.askyesno("Confirmar eliminación",
                                               "¿Está seguro de que desea eliminar esta contraseña?")
            if not confirmacion:
                return

            # Eliminar contraseña en la base de datos
            try:
                contrasenia_crud.delete_contrasenia(contrasena_id)
                messagebox.showinfo("Éxito", "La contraseña ha sido eliminada correctamente.")
                self.cargar_contrasenas()  # Refrescar la tabla después de eliminar
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar la contraseña: {e}")

        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al intentar eliminar la contraseña: {e}")
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
