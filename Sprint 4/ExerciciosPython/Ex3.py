from functools import reduce


def calcula_saldo(lancamentos) -> float:
    l = list(map(lambda x: x[0] if x[1] == 'C'  else -x[0], lancamentos))
    res = reduce(lambda x,y: x+y, l)
    return res


if __name__ == '__main__':
    lancamentos = [
        (200,'D'),
        (300,'C'),
        (100,'C')
    ]
    print(calcula_saldo(lancamentos))