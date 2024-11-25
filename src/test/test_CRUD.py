import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.modelo.modelo import Base, Usuario, Sesion
from src.logica.CRUD import UsuarioCRUD

class TestUsuarioCRUD(unittest.TestCase):
    def setUp(self):
        # Configuración de la base de datos en memoria para pruebas
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()

        # Crear un usuario de prueba
        usuario = Usuario(
            nombre_usuario="test_user",
            email="test@example.com",
            password_hash="hashed_password",
            rol="admin"
        )
        self.session.add(usuario)
        self.session.commit()

        self.usuario_crud = UsuarioCRUD(self.session)

    def tearDown(self):
        self.session.close()

    def test_iniciar_sesion_exitoso(self):
        # Probar iniciar sesión con credenciales válidas
        sesion = self.usuario_crud.iniciar_sesion("test@example.com", "hashed_password")
        self.assertIsNotNone(sesion)
        self.assertEqual(sesion.usuario.email, "test@example.com")

    def test_iniciar_sesion_fallido_email_incorrecto(self):
        # Probar iniciar sesión con un email incorrecto
        sesion = self.usuario_crud.iniciar_sesion("wrong@example.com", "hashed_password")
        self.assertIsNone(sesion)

    def test_iniciar_sesion_fallido_password_incorrecto(self):
        # Probar iniciar sesión con una contraseña incorrecta
        sesion = self.usuario_crud.iniciar_sesion("test@example.com", "wrong_password")
        self.assertIsNone(sesion)


if __name__ == "__main__":
    unittest.main()
