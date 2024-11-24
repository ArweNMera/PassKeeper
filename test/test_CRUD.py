import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.modelo import Base, Usuario, Sesion, Contrasenia, ContraseniaEtiqueta, Etiqueta
from src.logica.CRUD import UsuarioCRUD

class TestUsuarioCRUD(unittest.TestCase):
    def setUp(self):
        """Configuración antes de cada prueba"""
        # Crear una base de datos en memoria para las pruebas
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # Crear la instancia de la clase que vamos a probar, pasando la sesión
        self.usuario_crud = UsuarioCRUD(self.session)

    def tearDown(self):
        """Limpiar después de cada prueba"""
        self.session.close()

    def test_create_usuario(self):
        """Probar la creación de un usuario"""
        # Crear un usuario
        nombre_usuario = "user_test"
        email = "user_test@example.com"
        password_hash = "hashed_password"
        rol = "user"

        usuario = self.usuario_crud.create_usuario(nombre_usuario, email, password_hash, rol)

        # Verificar que el usuario fue creado correctamente
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.nombre_usuario, nombre_usuario)
        self.assertEqual(usuario.email, email)
        self.assertEqual(usuario.rol, rol)

    def test_create_usuario_duplicate_email(self):
        """Probar la creación de un usuario con un email duplicado"""
        # Crear un primer usuario
        nombre_usuario = "user_test"
        email = "user_test@example.com"
        password_hash = "hashed_password"
        rol = "user"

        self.usuario_crud.create_usuario(nombre_usuario, email, password_hash, rol)

        # Intentar crear un usuario con el mismo email
        with self.assertRaises(Exception):  # Aquí verificamos si se lanza una excepción
            self.usuario_crud.create_usuario("another_user", email, "hashed_password_2", "admin")
if __name__ == '__main__':
    unittest.main()