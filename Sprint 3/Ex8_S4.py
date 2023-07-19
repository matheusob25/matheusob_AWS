l = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 
for i in range(len(l)):
    if l[i][::-1] == l[i]:
        print('A palavra: {} é um palíndromo'.format(l[i]))
    else:
        print('A palavra: {} não é um palíndromo'.format(l[i]))

