class numero:
    def suma_indices(entrada, objetivo):
        indices = {}

        for i, n in enumerate(entrada):
            if objetivo - n in indices:
                return indices[objetivo - n], i
            
            indices[n] = i


numeros = [10,20,10,40,50,60,70]
objetivo = 50

salida = numero.suma_indices(numeros, objetivo)
print(salida) 