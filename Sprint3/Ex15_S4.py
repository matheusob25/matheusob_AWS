class Lampada: 
    
    def __init__(self, ligada):
        self.ligada = ligada

    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
    
    def esta_ligada(self):
        if self.ligada == True:
            return self.ligada
        else:
            return self.ligada      

if __name__ == '__main__':
    l1 = Lampada(ligada = False)
    l1.liga()
    print('A lâmpada está ligada? ',l1.esta_ligada())
    l1.desliga()
    print('A lâmpada está ligada? ',l1.esta_ligada())