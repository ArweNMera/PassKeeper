import tkinter as tk
from tkinter import messagebox, ttk

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#85929e")  # Fondo claro

        # Encabezado
        self.header = tk.Label(
            root,
            text="Bienvenido",
            font=("Arial", 16, "bold"),
            bg="#f0f0f5",
            fg="#333",
        )
        self.header.pack(pady=10)

        # Marco para el formulario
        self.frame_form = tk.Frame(root, bg="#ffffff", bd=2, relief="solid")
        self.frame_form.pack(pady=10, padx=20, fill="both", expand=True)

        # Etiquetas y campos de entrada
        self.label_email = tk.Label(
            self.frame_form, text="Correo Electrónico:", font=("Arial", 10), bg="#ffffff"
        )
        self.label_email.pack(pady=5, anchor="w")
        self.entry_email = ttk.Entry(self.frame_form, width=35)
        self.entry_email.pack(pady=5)

        self.label_password = tk.Label(
            self.frame_form, text="Contraseña:", font=("Arial", 10), bg="#ffffff"
        )
        self.label_password.pack(pady=5, anchor="w")
        self.entry_password = ttk.Entry(self.frame_form, width=35, show="*")
        self.entry_password.pack(pady=5)

        # Botones
        self.button_login = ttk.Button(
            self.frame_form, text="Iniciar Sesión"
        )
        self.button_login.pack(pady=10, fill="x", padx=20)

        self.button_register = ttk.Button(

        )
        self.button_register.pack(pady=5, fill="x", padx=20)

        # Pie de página
        self.footer = tk.Label(
            root,
            text="© 2024 - Tu Aplicación",
            font=("Arial", 8),
            bg="#f0f0f5",
            fg="#888",
        )
        self.footer.pack(pady=10)









if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
