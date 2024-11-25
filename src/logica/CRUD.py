#from pkg_resources import non_empty_lines
from sqlalchemy.exc import IntegrityError
#from sqlalchemy.orm import Session
#from datetime import datetime
from src.modelo.modelo import Usuario, engine, Sesion, Etiqueta, ContraseniaEtiqueta
#from src.config import sessionmaker
from datetime import datetime
from src.modelo.modelo import Contrasenia  # Asegúrate de importar correctamente el modelo Contrasenia

class Contraseniacrud:
    def __init__(self, session):
        self.session = session

    def create_contrasenia(self, servicio, nombre_usuario_servicio, contrasenia_encriptada, id_usuario, nota=None):
        """Crear una nueva contrasenia en la base de datos"""
        # Verificar si ya existe una contraseña para este servicio y usuario
       # existing_contrasenia = self.session.query(Contrasenia).filter_by(servicio=servicio, id_usuario=id_usuario).first()
       # if existing_contrasenia:
        #    raise Exception("Ya existe una contraseña para este servicio y usuario")

        contrasenia = Contrasenia(
            servicio=servicio,
            nombre_usuario_servicio=nombre_usuario_servicio,
            contrasenia_encriptada=contrasenia_encriptada,
            fecha_creacion=datetime.now(),
            #ultima_modificacion=datetime.now(),
            ultima_modificacion=None,
            id_usuario=id_usuario,
            nota=nota
        )
        self.session.add(contrasenia)
        self.session.commit()
        return contrasenia

    def get_contrasenias_by_user(self, id_usuario):
        """Obtener todas las contraseñas asociadas a un usuario"""
        return self.session.query(Contrasenia).filter_by(id_usuario=id_usuario).all()

    def editar_contrasena(self, id_contrasenia, contrasenia_encriptada=None, nota=None):
        """Actualizar los campos de una contrasenia"""
        contrasenia = self.session.query(Contrasenia).filter_by(id_contrasenia=id_contrasenia).first()
        if not contrasenia:
            raise Exception("La contraseña no existe")

        if contrasenia_encriptada:
            contrasenia.contrasenia_encriptada = contrasenia_encriptada
        if nota:
            contrasenia.nota = nota

        contrasenia.ultima_modificacion = datetime.now()
        self.session.commit()
        return contrasenia

    def delete_contrasenia(self, id_contrasenia):
        """Eliminar una contrasenia"""
        contrasenia = self.session.query(Contrasenia).filter_by(id_contrasenia=id_contrasenia).first()
        if not contrasenia:
            raise Exception("La contraseña no existe")

        self.session.delete(contrasenia)
        self.session.commit()

    def obtener_contrasenias_usuario(self, usuario_id):
        try:
            contrasenas = self.session.query(Contrasenia).filter(Contrasenia.id_usuario == usuario_id).all()
            return contrasenas
        except Exception as e:
            print(f"Error al obtener contraseñas: {e}")
            return []