import random

random_list = random.sample(range(500), 50)
random_list.sort()

mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0
media = sum(random_list)

meio1 = len(random_list) /2
meio2 = (len(random_list)/ 2) - 1
meio1 = int(meio1)
meio2 = int(meio2)
mediana = (random_list[meio2] + random_list[meio1]) / 2
valor_minimo = random_list[0]
valor_maximo = random_list[49]
print('Media: {}, Mediana: {}, Mínimo: {}, Máximo: {}'.format((media / 50),mediana, valor_minimo, valor_maximo))
