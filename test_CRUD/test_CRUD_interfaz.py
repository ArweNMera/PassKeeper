import unittest
from tkinter import messagebox
from src.vista.APP import RegisterWindow
import tkinter as tk

class TestRegisterWindow(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.root = tk.Tk()  # Crea la ventana principal de la aplicación
        self.app = RegisterWindow(self.root)  # Inicia la ventana de registro

    def tearDown(self):
        """Limpia los recursos después de cada prueba."""
        self.app.window.destroy()
        self.root.destroy()

    def test_register_user_success(self):
        """Prueba que se registre un usuario exitosamente."""
        # Simular la entrada de datos del usuario
        self.app.entry_username.insert(0, "usuario_test")
        self.app.entry_email.insert(0, "usuario@test.com")
        self.app.entry_password.insert(0, "contraseña123")
        self.app.entry_rol.insert(0, "admin")

        # Interceptar el mensaje de éxito con un mock
        def mock_register_user():
            self.app.register_user = lambda: messagebox.showinfo("Éxito", "Usuario registrado correctamente")

        self.app.register_user = mock_register_user()

        # Simula el clic en el botón Registrar
        self.app.button_register.invoke()

        # Asegurarse de que los datos ingresados estén correctos
        self.assertEqual(self.app.entry_username.get(), "usuario_test")
        self.assertEqual(self.app.entry_email.get(), "usuario@test.com")
        self.assertEqual(self.app.entry_password.get(), "contraseña123")
        self.assertEqual(self.app.entry_rol.get(), "admin")

    def test_register_user_missing_fields(self):
        """Prueba el mensaje de advertencia cuando faltan campos."""
        # Dejar algunos campos vacíos
        self.app.entry_username.insert(0, "")
        self.app.entry_email.insert(0, "usuario@test.com")
        self.app.entry_password.insert(0, "contraseña123")
        self.app.entry_rol.insert(0, "")

        # Interceptar el mensaje de advertencia
        def mock_register_user():
            self.app.register_user = lambda: messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

        self.app.register_user = mock_register_user()

        # Simula el clic en el botón Registrar
        self.app.button_register.invoke()

        # Asegurarse de que el mensaje de advertencia se muestra
        self.assertEqual(self.app.entry_username.get(), "")
        self.assertNotEqual(self.app.entry_email.get(), "")
        self.assertNotEqual(self.app.entry_password.get(), "")
        self.assertEqual(self.app.entry_rol.get(), "")

if __name__ == "__main__":
    unittest.main()
