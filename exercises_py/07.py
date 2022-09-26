class potencia:
    def potencia_numero(x, b):
        resultado = 1
        
        for i in range(b):
            resultado *= x
            
        return resultado
    

x = int(input("base:"))
b = int(input(" potencia:"))

print(potencia.potencia_numero(x, b)) 