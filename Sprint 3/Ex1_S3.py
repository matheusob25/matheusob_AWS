import datetime
nome = input('qual o seu nome: ')
idade = int(input('qual sua idade: '))
ano_100 = 100 - idade
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
print('ano que você fará 100 anos: {}'.format(date.year + ano_100))