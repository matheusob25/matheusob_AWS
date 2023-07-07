class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = 'azul'
        self.capacidade = capacidade

    def __str__(self):
        return f'O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima}, capacidade para {self.capacidade} passageiros e é da cor {self.cor}.'
    

if __name__ == '__main__':
    aviao1 = Aviao('BOIENG456', 1500, 400)
    aviao2 = Aviao('Embraer Praetor 600', 863, 14)
    aviao3 = Aviao('Antonov An-2', 258, 12)
    for aviao in [aviao1, aviao2, aviao3]:
        print(aviao)
       
  