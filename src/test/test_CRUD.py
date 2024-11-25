import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from src.modelo.modelo import Base, Usuario, Contrasenia
from src.logica.CRUD import Contraseniacrud

class TestContraseniacrud(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configurar la base de datos en memoria para todas las pruebas"""
        cls.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        """Configurar una nueva sesión antes de cada prueba"""
        self.session = self.Session()
        self.crud = Contraseniacrud(self.session)

        # Crear un usuario de prueba
        self.usuario = Usuario(
            nombre_usuario="test_user",
            email="test_user@example.com",
            password_hash="hashed_password",
            rol="usuario"
        )
        self.session.add(self.usuario)
        self.session.commit()

    def tearDown(self):
        """Limpiar la base de datos después de cada prueba"""
        self.session.query(Contrasenia).delete()
        self.session.query(Usuario).delete()
        self.session.commit()
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        """Eliminar la base de datos al finalizar todas las pruebas"""
        Base.metadata.drop_all(cls.engine)

    def test_create_contrasenia(self):
        """Probar la creación de una contraseña"""
        contrasenia = self.crud.create_contrasenia(
            servicio="Facebook",
            nombre_usuario_servicio="test_facebook_user",
            contrasenia_encriptada="encrypted_password",
            id_usuario=self.usuario.id_usuario,
            nota="Nota de prueba"
        )

        self.assertEqual(contrasenia.servicio, "Facebook")
        self.assertEqual(contrasenia.nombre_usuario_servicio, "test_facebook_user")
        self.assertEqual(contrasenia.contrasenia_encriptada, "encrypted_password")
        self.assertEqual(contrasenia.nota, "Nota de prueba")
        self.assertIsNotNone(contrasenia.fecha_creacion)

    def test_get_contrasenias_by_user(self):
        """Probar la obtención de contraseñas por usuario"""
        self.crud.create_contrasenia(
            servicio="Facebook",
            nombre_usuario_servicio="test_facebook_user",
            contrasenia_encriptada="encrypted_password",
            id_usuario=self.usuario.id_usuario
        )
        self.crud.create_contrasenia(
            servicio="Twitter",
            nombre_usuario_servicio="test_twitter_user",
            contrasenia_encriptada="another_encrypted_password",
            id_usuario=self.usuario.id_usuario
        )

        contrasenias = self.crud.get_contrasenias_by_user(self.usuario.id_usuario)
        self.assertEqual(len(contrasenias), 2)
        self.assertEqual(contrasenias[0].servicio, "Facebook")
        self.assertEqual(contrasenias[1].servicio, "Twitter")

    def test_editar_contrasena(self):
        """Probar la edición de una contraseña"""
        contrasenia = self.crud.create_contrasenia(
            servicio="Facebook",
            nombre_usuario_servicio="test_facebook_user",
            contrasenia_encriptada="encrypted_password",
            id_usuario=self.usuario.id_usuario
        )

        updated_contrasenia = self.crud.editar_contrasena(
            id_contrasenia=contrasenia.id_contrasenia,
            contrasenia_encriptada="updated_password",
            nota="Nota actualizada"
        )

        self.assertEqual(updated_contrasenia.contrasenia_encriptada, "updated_password")
        self.assertEqual(updated_contrasenia.nota, "Nota actualizada")
        self.assertIsNotNone(updated_contrasenia.ultima_modificacion)

    def test_delete_contrasenia(self):
        """Probar la eliminación de una contraseña"""
        contrasenia = self.crud.create_contrasenia(
            servicio="Facebook",
            nombre_usuario_servicio="test_facebook_user",
            contrasenia_encriptada="encrypted_password",
            id_usuario=self.usuario.id_usuario
        )

        self.crud.delete_contrasenia(contrasenia.id_contrasenia)

        contrasenias = self.crud.get_contrasenias_by_user(self.usuario.id_usuario)
        self.assertEqual(len(contrasenias), 0)


if __name__ == "__main__":
    unittest.main()
