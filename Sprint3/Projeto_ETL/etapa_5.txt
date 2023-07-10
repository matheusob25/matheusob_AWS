with open('actors.csv') as file:
      linhas = file.readlines() 

dados = []
for linha in linhas[1:]:
    valores = []
    valores_recorrentes = ""
    aspas = False
    
    for char in linha:
        if char == ',' and not aspas:
            valores.append(valores_recorrentes.strip('"'))
            valores_recorrentes = ""
        else:
            valores_recorrentes += char
        
        if char == '"':
            aspas = not aspas
    
    valores.append(valores_recorrentes.strip('"'))
    
    dados.append((valores[0], float(valores[1])))
    dados_ordenados = sorted(dados, key=lambda x: x[1])[::-1]
   

for dado in dados_ordenados:
    nome, rendimento = dado
    print(f"{nome}, {rendimento}")