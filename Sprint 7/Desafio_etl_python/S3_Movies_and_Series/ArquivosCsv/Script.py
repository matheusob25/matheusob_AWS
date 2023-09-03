import csv
import boto3

s3 = boto3.client('s3', region_name='us-east-1',aws_access_key_id='AKIA3AUF5KDIHD2YSJD5', aws_secret_access_key='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')

bucket = 'moviesandseries025'



arquivos_csv = [
    {'nome': '/app/arq/movies.csv', 'caminho_s3': 'Raw/Local/CSV/Movies/2023/09/02/movies.csv'},
    {'nome': '/app/arq/series.csv', 'caminho_s3': 'Raw/Local/CSV/Series/2023/09/02/series.csv'}
]

for arquivo in arquivos_csv:
    nome_arquivo = arquivo['nome']
    caminho_s3 = arquivo['caminho_s3']

    with open(nome_arquivo, 'r') as csv_file:
        csv_content = csv_file.read()

   
    s3.put_object(Bucket=bucket, Key=caminho_s3, Body=csv_content)
    print(f"Arquivo {nome_arquivo} carregado para o S3 no caminho: s3://{bucket}/{caminho_s3}")
