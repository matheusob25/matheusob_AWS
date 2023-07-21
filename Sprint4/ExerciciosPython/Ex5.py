import csv

def ler_arquivo_csv(nome_arquivo):
    alunos_notas = []
    with open(nome_arquivo, newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            nome_aluno = linha[0]
            notas = list(map(int, linha[1:]))
            alunos_notas.append({'Nome': nome_aluno, 'Notas': notas})
    return alunos_notas

def calcular_media_tres_melhores(notas_aluno):
    notas_ordenadas = sorted(notas_aluno, reverse=True)[:3]
    media_tres_melhores = round(sum(notas_ordenadas) / 3, 2)
    return media_tres_melhores

def tres_melhores_notas(notas_aluno):
    notas_ordenadas = sorted(notas_aluno, reverse=True)[:3]
    return notas_ordenadas

arquivo_csv = "estudantes.csv"
dados_alunos = ler_arquivo_csv(arquivo_csv)
alunos_ordenados= sorted(dados_alunos, key=lambda aluno: aluno['Nome'])

for aluno in alunos_ordenados:
    media_tres_melhores = calcular_media_tres_melhores(aluno['Notas'])
    notas_ordenadas = tres_melhores_notas(aluno['Notas'])
    print(f"Nome: {aluno['Nome']} Notas: {notas_ordenadas} Média: {media_tres_melhores}")
