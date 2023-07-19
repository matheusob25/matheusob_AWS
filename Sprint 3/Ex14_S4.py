def funcao(*arg,**args):
    for a in arg:
        print(a)
    for v in args.values():
        print(v)

funcao(1, 3, 4, 'hello', parametro_nomeado = 'alguma coisa', x = 20)

