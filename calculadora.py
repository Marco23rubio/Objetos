import math

class Calculadora:
    def __init__(self,numero) -> None:
        self.numero = numero
        #self.datos = [5 for i in range(self.numero)]
        #self.datos = 0

    def IngresarDato(self):
        self.numero = [int(input("Ingresar datos " +str(i+1)+" = "))for i in range(self.numero)]

class Op_basicas(Calculadora):
    def __init__(self) -> None:
        Calculadora.__init__(self,3)

    def Suma (self):
        a,b, = self.numero
        s = a+b 
        print("El resultado es: ",s)
    
    def Resta (self):
        a,b, = self.numero
        r = a-b 
        print("El resultado es: ",r)

class Raiz(Calculadora):
    def __init__(self) -> None:
        Calculadora.__init__(self,1)

    def cuadrada(self):
        a, = self.numero
        print("El resultado es: ",math.sqrt(a))

ejemplo = Op_basicas()
print(ejemplo.IngresarDato())
print(ejemplo.Suma())

