arquivo_txt = "number.txt"
with open(arquivo_txt, 'r') as arquivo:
    linhas = arquivo.readlines()

    numeros = []
    for linha in linhas:
        numero = linha.split()
        numeros_linha = list(map(int,numero))
        numeros.extend(numeros_linha)

    numeros_do_arquivo = numeros


order = list(filter(lambda x: x % 2 == 0, numeros_do_arquivo))
cinco_maiores = sorted(order, reverse=True)[:5]


   
res = cinco_maiores
    
print('{}'.format(cinco_maiores))
print('{}'.format(sum(res)))

