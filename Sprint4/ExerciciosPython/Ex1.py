def ler_arquivo_numeros(nome):
    try:
        with open(nome, 'r') as arquivo:
            linhas = arquivo.readlines()

        numeros = []
        for linha in linhas:
            numero = linha.split()
            numeros_linha = list(map(int,numero))
            numeros.extend(numeros_linha)

        return numeros

    except FileNotFoundError:
        print(f"O arquivo '{nome}' não foi encontrado.")
        return []


def filtrando_num(num):
    order = list(filter(lambda x: x % 2 == 0, num))
    cinco_maiores = sorted(order, reverse=True)[:5]

    return cinco_maiores

def soma(s):
    soma = sum(s)
    return soma

if __name__ == "__main__":

    arquivo_txt = "number.txt"
    numeros_do_arquivo = ler_arquivo_numeros(arquivo_txt)
    order = filtrando_num(numeros_do_arquivo)
    
    print('-{}'.format(order))
    print('-{}'.format(soma(order)))

