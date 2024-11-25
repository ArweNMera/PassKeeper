import unittest
from tkinter import ttk
from unittest.mock import MagicMock
import tkinter as tk
from src.vista.APP import LoginWindow  # Asegúrate de guardar la clase en un archivo llamado login_window.py


class TestLoginWindow(unittest.TestCase):
    def setUp(self):
        """Configurar la interfaz antes de cada prueba."""
        self.root = tk.Tk()
        self.app = LoginWindow(self.root)

    def tearDown(self):
        """Destruir la interfaz después de cada prueba."""
        self.root.destroy()

    def test_widgets_existen(self):
        """Verificar que todos los widgets necesarios están presentes."""
        self.assertIsInstance(self.app.header, tk.Label)
        self.assertIsInstance(self.app.frame_form, tk.Frame)
        self.assertIsInstance(self.app.label_email, tk.Label)
        self.assertIsInstance(self.app.entry_email, tk.Entry)
        self.assertIsInstance(self.app.label_password, tk.Label)
        self.assertIsInstance(self.app.entry_password, tk.Entry)
        self.assertIsInstance(self.app.button_login, ttk.Button)
        self.assertIsInstance(self.app.footer, tk.Label)

    def test_botones_funcionan(self):
        """Simular clics en los botones y verificar las acciones."""
        # Simular el botón "Iniciar Sesión"
        self.app.button_login.invoke()
        # No hay acción definida para este botón en el código actual, así que no verificamos comportamiento.

        # Simular el botón "Registrarse" (agregar acción si se define en el futuro)
        self.app.button_register.invoke()

    def test_ingreso_datos(self):
        """Simular el ingreso de datos en los campos de entrada."""
        email = "test@example.com"
        password = "password123"

        # Simular entrada de texto
        self.app.entry_email.insert(0, email)
        self.app.entry_password.insert(0, password)

        # Verificar que los datos se hayan insertado correctamente
        self.assertEqual(self.app.entry_email.get(), email)
        self.assertEqual(self.app.entry_password.get(), password)


if __name__ == "__main__":
    unittest.main()
