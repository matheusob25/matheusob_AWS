a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
c = []
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
          c.append(b[j])


lista_final = list(set(c))
print(lista_final)

