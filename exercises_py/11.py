
from math import pi

class circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        resultado_area = pi*(self.radio**2)
        return resultado_area
    
    def perimetro(self):
        resultado_perimetro = 2*pi*self.radio
        return resultado_perimetro
    
radio = int(input("Ingresa la medida del radio del circulo: "))
medidas = circulo(radio)

print("El area del circulo es: ", medidas.area())
print("El perimetro del circulo es: ", medidas.perimetro())