from pkg_resources import non_empty_lines
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from datetime import datetime
from src.modelo.modelo import Usuario, engine, Sesion, Etiqueta, ContraseniaEtiqueta
from src.config import sessionmaker
from datetime import datetime
from src.modelo.modelo import Contrasenia  # Asegúrate de importar correctamente el modelo Contrasenia

class UsuarioCRUD:
    def __init__(self, session):
        self.session = session

    def create_usuario(self, nombre_usuario, email, password_hash, rol):
        """Crear un nuevo usuario"""
        try:
            nuevo_usuario = Usuario(
                nombre_usuario=nombre_usuario,
                email=email,
                password_hash=password_hash,
                rol=rol
            )
            self.session.add(nuevo_usuario)
            self.session.commit()
            return nuevo_usuario
        except IntegrityError:
            self.session.rollback()  # Rollback en caso de error (por ejemplo, email duplicado)
            raise Exception("El email ya está registrado.")