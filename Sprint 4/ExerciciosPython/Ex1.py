# nesse código eu fiz com funções, mas ele não retorna nada na udemy, então na udemy eu fiz sem nenhuma função e funcionou, alguns outros exercícios eu modifiquei também para passar na udemy mas estão bem parecidos

def ler_arquivo_numeros(nome):
        with open(nome, 'r') as arquivo:
            linhas = arquivo.readlines()

        numeros = []
        for linha in linhas:
            numero = linha.split()
            numeros_linha = list(map(int,numero))
            numeros.extend(numeros_linha)

        return numeros

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
    
    print('{}'.format(order))
    print('{}'.format(soma(order)))

