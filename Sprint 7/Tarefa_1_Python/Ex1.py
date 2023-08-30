import pandas as pd


if __name__ == "__main__":
    try:
        df = pd.read_csv("actors.csv", encoding="UTF-8", delimiter=",")

        maior_num_film = df["Number of Movies"].idxmax()
        media = df["Number of Movies"].mean()
        filmes_repetidos = df["#1 Movie"].value_counts()
        media_por_filme = df["Average per Movie"].idxmax()

        nome_maior_num = df.loc[maior_num_film, "Actor"]
        num_de_filmes = df.loc[maior_num_film, "Number of Movies"]
        nome_media_filme = df.loc[media_por_filme, "Actor"]
        fil_mais_repetido = filmes_repetidos[filmes_repetidos == filmes_repetidos.max()]

        print(f"Nome do ator com a maior quantidade de filmes: {nome_maior_num} \nquantidade de filmes: {num_de_filmes}")
        print(f"Média da quantidade de filmes de cada ator: {media}")
        print(f"Nome do ator com a maior média por filme:  {nome_media_filme}")
        for item, res in fil_mais_repetido.items():
            print(f"Filme mais frequente: {item}\nFrequência: {res} ")

    except pd.errors.EmptyDataError:
         print("Seu arquivo está vazio ou não pode ser lido")
