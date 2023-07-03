import json

with open('person.json', 'r')as arquivo: 
    pessoa = json.load(arquivo)

print(pessoa)