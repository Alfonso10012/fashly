from  werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self,id,nombre,apellido,correo,clave,telefono,fechareg,perfil)-> None:
        self.id         = id
        self.nombre     = nombre
        self.apellido   = apellido
        self.correo     = correo
        self.clave      = clave
        self.telefono   = telefono
        self.fechareg   = fechareg
        self.perfil     = perfil
        
    @classmethod
    def validarClave(self,claveCifrada,clave):
        return check_password_hash(claveCifrada,clave)


