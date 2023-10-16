import json
import requests
import boto3
import os
import botocore.exceptions

def lambda_handler(arg, context):
    api_key = os.environ['api_key']
    aws_secret_access_key = os.environ['aws_secret_access_key']
    aws_id = os.environ['aws_access_key_id']
    
    url = f"https://api.themoviedb.org/3/find/tt0120737?external_source=imdb_id&api_key={api_key}&language=PT_BR"
    s3 = (boto3.client('s3', region_name='us-east-1',aws_access_key_id=aws_id ,aws_secret_access_key=aws_secret_access_key))
    
    bucket = 'moviesandseries025'
    
    response = requests.get(url)
    
    filme = []
    if response.status_code == 200:
        data = response.json()
    
        for movie in data['movie_results']:
            titulo = movie.get('title', None)
            data_lancamento = movie.get('release_date', None)
            visao_geral = movie.get('overview', None)
            votos = movie.get('vote_count', None)
            media_votos = movie.get('vote_average', None)
            popularidade = movie.get('popularity', None)

            df = {'Titulo': titulo,
                  'Data de lancamento': data_lancamento,
                  'Visão geral': visao_geral,
                  'Votos': votos,
                  'Média de votos:': media_votos,
                  'Popularidade': popularidade}
            filme.append(df)

    else:
        return f'Erro na solicitação: {response.status_code}'
    
    resul = json.dumps(filme)
    caminho = 'Raw/TMDB/Json/2023/09/08/LordOfTheRings1.json'
    try:
        s3.put_object(Bucket= bucket, Key= caminho, Body= resul)   
        return 'arquivo json enviado com sucesso'
    except botocore.exceptions.ClientError as e:
        return f'erro ao enviar arquivo:{str(e)} '
    
    
