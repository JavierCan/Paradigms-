
class evaluation :
    def parentesis_valido (cadena) :
        lista = [] 
        parentesis = {'{': '}', '(': ')', '[': ']'} # diccionario

        for x in cadena : # iteraccion  cada caracter 
            if x in parentesis :
                lista.append(x) # agrega el elemento a la lista
            elif len( lista) == 0 or x  != parentesis[lista.pop()] : # si el elemento no se encuentra con el metodo pop o no es igual  0
                return False
        return len( lista)  == 0 # evaluacion de un solo elemento
cadena = input("ingrese los parentesis") 
print (evaluation.parentesis_valido(cadena))     
