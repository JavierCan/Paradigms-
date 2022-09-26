class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        resultado = self.base * self.altura

        return resultado

base = int(input("Ingrese las medidas de la base: "))
altura = int(input("Ingrese las medidas de la altura: "))
medidas = rectangulo(base, altura)


print("El área del rectangulo es = ", medidas.area())