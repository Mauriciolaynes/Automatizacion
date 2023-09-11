class calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range (numero)]

    def ingresardato (self):
        self.datos = [int(input("Ingresar datos " + str(i+1)+ " = ")) for i in range (self.n)]

    
class op_basicas(calculadora):
    def __init__(self):
        calculadora.__init__(self,2)

    def suma(self):
        a,b = self.datos
        s = a + b
        print("El resultado es:" , s)

    def resta(self):
        a,b = self.datos
        s = a - b
        print("El resultado es:" , s)
    
    def multi(self):
        a,b = self.datos
        s = a * b
        print("El resultado es:" , s)   

    def divi(self):
        a,b = self.datos
        s = a / b
        print("El resultado es:" , s)  

class raiz (calculadora):
    def __init__(self):
        calculadora.__init__(self,1)
    def cuadrada(self):
        import math
        a, = self.datos
        print("El resultado es: " , math.sqrt(a))


"""ejemplo = raiz()
print(ejemplo.ingresardato())
print(ejemplo.cuadrada())"""

objeto = op_basicas()

print(isinstance(objeto,op_basicas))