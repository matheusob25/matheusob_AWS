numero = [0,0,0]


for i in range(len(numero)):
    numero[i] = int(input('digite o {}º número: '.format(i + 1)))
    
for a in range(len(numero)):
    if numero[a] % 2 == 0:
        print('Par: {}'.format(numero[a]))
    else:
        print('Ímpar: {}'.format(numero[a]))