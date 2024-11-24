import tkinter as tk
from tkinter import messagebox, ttk
from sqlalchemy.orm import sessionmaker
#from src.logica.CRUD import UsuarioCRUD, Contraseniacrud
from datetime import datetime
import random
import string

class RegisterWindow:
    def __init__(self, parent):
        self.register_user = None
        self.generate_password = None
        self.window = tk.Toplevel(parent)
        self.window.title("Registrar Usuario")
        self.window.geometry("400x450")
        self.window.resizable(False, False)
        self.window.configure(bg="#85929e")  # Fondo de la ventana

        # Encabezado
        self.label_title = tk.Label(
            self.window,
            text="Registro de Usuario",
            font=("Helvetica", 16, "bold"),
            bg="#f5f5f5",
            fg="#333333"
        )
        self.label_title.pack(pady=15)

        # Marco del formulario
        self.form_frame = tk.Frame(self.window, bg="#ffffff", bd=2, relief="groove")
        self.form_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Campo: Nombre de Usuario
        self.label_username = tk.Label(
            self.form_frame,
            text="Nombre de Usuario:",
            font=("Helvetica", 10),
            bg="#ffffff"
        )
        self.label_username.pack(pady=5, anchor="w", padx=10)
        self.entry_username = ttk.Entry(self.form_frame, width=30)
        self.entry_username.pack(pady=5, padx=10)

        # Campo: Correo Electrónico
        self.label_email = tk.Label(
            self.form_frame,
            text="Correo Electrónico:",
            font=("Helvetica", 10),
            bg="#ffffff"
        )
        self.label_email.pack(pady=5, anchor="w", padx=10)
        self.entry_email = ttk.Entry(self.form_frame, width=30)
        self.entry_email.pack(pady=5, padx=10)

        # Campo: Contraseña
        self.label_password = tk.Label(
            self.form_frame,
            text="Contraseña:",
            font=("Helvetica", 10),
            bg="#ffffff"
        )
        self.label_password.pack(pady=5, anchor="w", padx=10)
        self.entry_password = ttk.Entry(self.form_frame, width=30, show="*")
        self.entry_password.pack(pady=5, padx=10)

        # Botón: Generar Contraseña
        self.button_generate_password = ttk.Button(
            self.form_frame,
            text="Generar Contraseña",
            command=self.generate_password
        )
        self.button_generate_password.pack(pady=5, padx=10)

        # Campo: Rol
        self.label_rol = tk.Label(
            self.form_frame,
            text="Rol (admin, usuario):",
            font=("Helvetica", 10),
            bg="#ffffff"
        )
        self.label_rol.pack(pady=5, anchor="w", padx=10)
        self.entry_rol = ttk.Entry(self.form_frame, width=30)
        self.entry_rol.pack(pady=5, padx=10)

        # Botón: Registrar
        self.button_register = ttk.Button(
            self.form_frame,
            text="Registrar",
            command=self.register_user
        )
        self.button_register.pack(pady=15, padx=10)



if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterWindow(root)
    root.mainloop()
