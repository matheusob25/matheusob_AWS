class Pessoa:
    def __init__(self, id):
        self.__nome = None
        self.id = id

    def set_nome(self, __nome):
        self.__nome = __nome

    def get_nome(self):
        return self.__nome


if __name__ == '__main__':
    pessoa = Pessoa(0)
    pessoa.set_nome('Fulano de Tal')
    print(pessoa.get_nome())
