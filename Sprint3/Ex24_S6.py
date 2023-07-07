class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        self.listaBaguncada = sorted(self.listaBaguncada)
        crescente = self.listaBaguncada
        return crescente
    
    def ordenacaoDecrescente(self):
        self.listaBaguncada = sorted(self.listaBaguncada)
        decrescente = self.listaBaguncada[::-1]
        return decrescente
    
if __name__ == '__main__':
    o1 = Ordenadora([3,4,2,1,5])
    o2 = Ordenadora([9,7,6,8])
    print(o1.ordenacaoCrescente())
    print(o2.ordenacaoDecrescente())