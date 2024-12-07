from abc import ABC, abstractmethod

class Auth(ABC):
    @abstractmethod
    def iniciarSesion(self, usuario, password):
        pass

class Autenticacion(Auth):
    def iniciarSesion(self, usuario, password):
        print(f"Iniciando sesión con el usuario: {usuario}")

class DecoradorAuth(Auth):
    def __init__(self, componente: Auth):
        self._componente = componente 

    def iniciarSesion(self, usuario, password):
        self._componente.iniciarSesion(usuario, password)

class SoporteGmail(DecoradorAuth):
    def iniciarSesion(self, usuario, password):
        print(f"Verificando correo: {usuario}")
        if "@gmail.com" not in usuario:
            print("Error, solo soporta cuentas de Gmail")
        else:
            print("Validación de Gmail exitosa")
            super().iniciarSesion(usuario, password)

class SoporteFacebook(DecoradorAuth):
    def iniciarSesion(self, usuario, password):
        print(f"Verificando usuario de Facebook: {usuario}")
        if not usuario.isalnum():
            print("Error,solo soporta usuarios con letras y números")
        else:
            print("Validación de Facebook exitosa")
            super().iniciarSesion(usuario, password)

autenticador = Autenticacion()

ag = SoporteGmail(autenticador)
ag.iniciarSesion("abril@gmail.com", "ab0715")
print("\n")
ag.iniciarSesion("abril@hotmail.com", "ab2408")
print("\n")

af = SoporteFacebook(autenticador)
af.iniciarSesion("AbrilGodoy175", "2809a")
print("\n")
af.iniciarSesion("usuario&+inválido", "shdjskd8")