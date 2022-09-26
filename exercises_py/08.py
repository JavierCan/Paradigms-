class inversion:
    def invertir(texto):
        textoinvertido  = ' '.join(reversed(oracion.split()))
        return textoinvertido
    
oracion = 'Mi Diario Python'

print(oracion)
print(inversion.invertir(oracion)) 