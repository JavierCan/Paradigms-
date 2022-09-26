class subconjuntos1:
    def subconjuntos(entrada):
        return subconjuntos_recursivo([], sorted(entrada))

def subconjuntos_recursivo(actual, conjunto):
    if conjunto:
        return subconjuntos_recursivo(actual, conjunto[1:]) + subconjuntos_recursivo(actual + [conjunto[0]], conjunto[1:])
    return [actual]


entrada = [4, 5, 6]
resultado = subconjuntos1.subconjuntos(entrada)

print(resultado)