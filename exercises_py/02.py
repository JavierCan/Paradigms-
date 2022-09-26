# jesus javier can noh 
class numbers :  
    def romano_a_entero(datoromano): #metodo de conversion 
        romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100} #diccionario 
        entero   = 0 

        for i in range(len(datoromano)): # se saca la longitud del arreglo para la cantidad de iteraciones segun 'datoromano'
            if i > 0 and romanos[datoromano[i]] > romanos[datoromano[i - 1]]: # comprobacion mayor a cero y mayor al numero anterior 
                entero += romanos[datoromano[i]] - 2 * romanos[datoromano[i - 1]] # se le resta el anterior 
            else:
                entero += romanos[datoromano[i]] # si no se cumple la condicion se concatena el valor de i al entero 
        
        return entero
datoromano = input("Ingrese un número romano ( MAYUSCULAS ) : ") # entrada de datos 
print(numbers.romano_a_entero(datoromano))

