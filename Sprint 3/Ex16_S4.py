def soma(st):
    som = 0
    string = st
    string = string.split(',')
    for i in range(len(string)):
        som += int(string[i])
    return som  


str = "1,3,4,6,10,76"
print(soma(str))

