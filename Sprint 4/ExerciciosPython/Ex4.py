def calcular_valor_maximo(operadores,operandos) -> float:
    resultado_zip = [(x,op,y)for (x, y), op in zip(operandos,operadores) ]
    resultado_map = list(map(lambda x: eval(f'{x[0]}{x[1]}{x[2]}'), resultado_zip)) # utilizei o eval aqui por ser um código com uma dimensão pequena e sem riscos
    maior_valor = max(resultado_map)
    return maior_valor

if __name__ == '__main__':
    op = ['+', '-', '*', '/', '%']
    valores = [(10, 20), (30, 40), (4.9, 2.1), (100, 3), (5, 2)]
    print(calcular_valor_maximo(op,valores))