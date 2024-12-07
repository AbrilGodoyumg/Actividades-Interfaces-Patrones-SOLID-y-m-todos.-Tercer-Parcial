class Empleado:
    bonificaciong_fija = 300

    def __init__(self, nombre, antiguedad, salario_base):
        self.__nombre = nombre
        self.__antiguedad = antiguedad
        self.__salario_base = salario_base

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def antiguedad(self):
        return self.__antiguedad

    @antiguedad.setter
    def antiguedad(self, valor):
        if valor < 0:
            raise ValueError("La antigüedad incorrecta.")
        self.__antiguedad = valor

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, valor):
        if valor < 0:
            raise ValueError("El salario base es incorrecto.")
        self.__salario_base = valor

    @classmethod
    def calcular_bonificaciong(cls):
        return cls.bonificaciong_fija

    def calcular_bonificaciona(self):
        return self.__antiguedad * 100

    def calcular_bonificacion_total(self):
        return self.calcular_bonificaciong() + self.calcular_bonificaciona()


e1 = Empleado("Abril Godoy", 7, 1000)

print(f"Nombre del empleado: {e1.nombre}")
print(f"Antigüedad: {e1.antiguedad}")
print(f"Salario base: ${e1.salario_base}")

bonificaciong = Empleado.calcular_bonificaciong()
print(f"Bonificación general: ${bonificaciong}")

bonificaciona = e1.calcular_bonificaciona()
print(f"Bonificación por antigüedad: ${bonificaciona}")

bonificacion_total = e1.calcular_bonificacion_total()
print(f"Bonificación total: ${bonificacion_total}")