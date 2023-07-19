primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i,(primeirosNomes,sobreNomes,idades) in enumerate(zip(primeirosNomes, sobreNomes,idades)):
    print('{} - {} {} está com {} anos'.format(i,primeirosNomes,sobreNomes,idades))