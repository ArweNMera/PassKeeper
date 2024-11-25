from sqlalchemy.exc import IntegrityError
from src.modelo.modelo import Usuario, Sesion, Etiqueta, ContraseniaEtiqueta
from datetime import datetime
from src.modelo.modelo import Contrasenia  # Asegúrate de importar correctamente el modelo Contrasenia

class UsuarioCRUD:
    def __init__(self, session):
        self.session = session

    def iniciar_sesion(self, email, password_hash):
        """Iniciar sesión con un usuario basado en el correo y la contraseña proporcionados"""
        usuario = self.session.query(Usuario).filter_by(email=email).first()
        if usuario and usuario.password_hash == password_hash:
            # Crear una sesión para el usuario
            sesion = Sesion(id_usuario=usuario.id_usuario, fecha_inicio=datetime.now())
            self.session.add(sesion)
            self.session.commit()
            return sesion  # Retornar la sesión creada
        return None