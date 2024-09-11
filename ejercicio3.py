class Circulo:
    def __init__(self,radio):
        self.__radio = radio
        self.__pi = 3.1415
    
    def calcularPerimetro(self):
        return 2*self.__pi*self.__radio
    
    def calcularArea(self):
        return self.__pi*self.__radio**2
    
    def getPi(self):
        return self.__pi
    
    
    def setRadio(self,nuevoValor):
        if type(nuevoValor) == int or type(nuevoValor) == float:
            if nuevoValor > 0:
                self.radio = nuevoValor
                print(f"El radio se a modificado correctamente: {self.__radio}")
            else:
                print("el radio no puede ser negativo")
        
        else:
            print("el radio tiene que ser un numero")

c1 = Circulo(2.5)
print(c1.calcularArea())
print(c1.calcularPerimetro())
print(f"la constante pi es {c1.getPi()}")
c1.setRadio(25)
c1.setRadio(-4)
c1.setRadio("hoolaquetal")


