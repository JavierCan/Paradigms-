
# jesus javier can noh 

class numbers: # creamos una clase para luego asignarle una peticion de datos con un metodo
    def conversion(dato):  # mtodo conversion 
        num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] # diccionario 1
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'] # diccionario 2
    
        romano = '' 
        i = 0
    
        while dato > 0: 
            for x  in range(dato // num[i]): # los numeros se dividen para poder  recorrer el diccionario 1 
                romano += roman[i] # se concatena la posicion i del diccionario 2 a 'romanos'
                dato  -= num[i] # se le mquita la posicion 1 para poder regresar al ciclo 
    
            i += 1 # se le agrega 1 para hacer nuevamente e recorrido del diccionrio 1 
        
        return romano # valor concatenado

dato = int(input("Ingrese un número")) # entrada de datos 
if dato  > 0: 
    print(numbers.conversion(dato)) 