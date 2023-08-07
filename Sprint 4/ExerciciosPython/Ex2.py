def conta_vogais(texto:str)-> int:
    texto = texto.lower()
    vogais = ['a','e','i','o','u']
    vogais_encontradas = list(filter(lambda x: x in vogais, texto))
    quantidade = len(vogais_encontradas)
    return quantidade


if __name__ == '__main__':
    texto = input('Digite um texto: ')
    print(conta_vogais(texto))