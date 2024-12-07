class CuentaBancaria:
    def __new__ (cls, *args, **kwargs):
        instancia=super(CuentaBancaria,cls).__new__(cls)
        return instancia
    
    @classmethod
    def numero(cls,num_cuenta):
        instancia=cls.__new__(cls) #Instancia vacia
        #Atributos
        instancia.num_cuenta=num_cuenta
        instancia.saldo=0
        instancia.tipo_cuenta="corriente"
        return instancia
    
    @classmethod
    def numero_saldo(cls,num_cuenta,saldo_inicial):
        instancia=cls.__new__(cls) #Instancia vacia
        #Atributos
        instancia.num_cuenta=num_cuenta
        instancia.saldo=saldo_inicial
        instancia.tipo_cuenta="corriente"
        return instancia
    
    @classmethod
    def numero_saldo_tipocuenta(cls,num_cuenta,saldo_inicial,tipo_cuenta):
        instancia=cls.__new__(cls) #Instancia vacia
        #Atributos
        instancia.num_cuenta=num_cuenta
        instancia.saldo=saldo_inicial
        instancia.tipo_cuenta=tipo_cuenta
        return instancia
    
    def __repr__(self):
        return f"CuentaBancaria: Numero de cuenta= {self.num_cuenta}, Saldo= {self.saldo}, Tipo de cuenta= {self.tipo_cuenta}"
    
c1= CuentaBancaria.numero("1257")
c2= CuentaBancaria.numero_saldo("1257",2500)
c3= CuentaBancaria.numero_saldo_tipocuenta("1257",2500,"Ahorros")

print(c1)
print(c2)
print(c3)