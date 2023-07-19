def listas(l):
    lista = l
    tam = len(lista) // 3
    lista1,lista2,lista3, lista4 = [],[],[],[]
    for i in lista:
        if i <= tam:
            lista1.append(i)
        elif i <= (tam + tam):
            lista2.append(i)
        elif i <= (tam + tam + tam):
            lista3.append(i)
    
    lista4.append(lista1)
    lista4.append(lista2)
    lista4.append(lista3)
    return lista4 
    


lista1 = listas
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(lista1(lista))
