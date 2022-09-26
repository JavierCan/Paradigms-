from itertools import combinations

class suma:
    def suma_cero(entrada):
        sub_tres = list(combinations(entrada, 3))
        sublistas = []

        for i in sub_tres:
            if sum(i) == 0:
                sublistas.append(i)
        
        return sublistas

entrada = [-25, -10, -7, -3, 2, 4, 8, 10]
resultado = suma.suma_cero(entrada)

print(resultado)