class Passaro:
    def __init__(self, nome,voando = False):
        self.nome = nome
        self.voando = voando
        
    def __str__(self):
        return f'{self.nome}'
    
    def voar(self):
        self.voando = True
        if self.voando:
            return 'Voando...'
    
    def emitir_som(self):
        return f'{self.nome} emitindo som...'


class Pato(Passaro):
    def __init__(self,nome,voando = False):
        super().__init__(nome,voando)

    def __str__(self):
        return super().__str__()
    
    def voar(self):
        return super().voar()
    
    def emitir_som(self):
        return super().emitir_som()
    
    def barulho(self):
        return 'Quack Quack'
    
class Pardal(Passaro):
    def __init__(self,nome,voando = False):
        super().__init__(nome,voando)

    def __str__(self):
        return super().__str__()
    
    def voar(self):
        return super().voar()
    
    def emitir_som(self):
        return super().emitir_som()
    
    def baruho(self):
        return 'Piu Piu'
    

if __name__ == '__main__':
    p1 = Pato('Pato')
    print(p1)
    print(p1.voar())
    print(p1.emitir_som())
    print(p1.barulho())
    p2 = Pardal('Pardal')
    print(p2)
    print(p2.voar())
    print(p2.emitir_som())
    print(p2.baruho())