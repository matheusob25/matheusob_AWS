list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def exp(va1, va2):       # sei que já existe a pow de math mas resolvi criar essa função só pra treinar um pouco essas funções
    var3 = va1 ** va2

    return var3


def my_map(lista, exp):
    resultado = []
    for a in lista:
        resultado.append(exp(a,2))
    
    return resultado

print(my_map(list, exp))