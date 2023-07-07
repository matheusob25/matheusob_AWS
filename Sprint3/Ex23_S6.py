class Calculo:
    def soma(x,y):
        return f'Somando:{x} + {y} = {x+y}'
    
    def subtracao(x,y):
        return f'Subtraindo:{x} - {y} = {x-y}'
    
if __name__ == '__main__':
    print(Calculo.soma(4,5))
    print(Calculo.subtracao(4,5))