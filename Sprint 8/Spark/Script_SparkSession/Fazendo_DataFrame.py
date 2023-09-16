import random
import time
import names
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import expr, col

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("Exercicio_txt") \
        .getOrCreate()

    df_nomes = spark.read.csv("nomes.txt", header=False)
    df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
    df_nomes = df_nomes.withColumn("Escolaridade", expr("array('Medio','Fundamental','Superior')[int(rand() * 3)]"))
    df_nomes = df_nomes.withColumn("País", expr("array('Colômbia','Brasil','Argentina','Peru','Uruguai','Equador','Guiana','Chile','Guiana Francesa', 'Suriname','Paraguai','Bolívia','Venezuela')[int(rand() * 13)]"))
    ano1 = 1945
    ano2 = 2010
    df_nomes = df_nomes.withColumn("AnoNascimento", expr(f"int(rand() * ({ano2 + 1 - ano1})) + {ano1} "))
    df_select = df_nomes.select('*').where(col('AnoNascimento') >= 2001)


    # Etapa 8
    quant_pessoas_milenium = df_nomes.select('*').filter((col('AnoNascimento') >= 1980) & (col('AnoNascimento') <= 1994)).count()
    print(f'Essa é a quantidade de pessoas da geração milenium que nasceram entre 1980 e 1994 : {quant_pessoas_milenium}')

    # Etapa 9
    df_nomes.createOrReplaceTempView("pessoas")
    spark.sql('select count(*) as Millennials from pessoas where AnoNascimento between 1980 and 1994').show()



    #etapa 10
    consulta = """
        select
            `pessoas`.`País` as Pais,
            case
                when AnoNascimento between 1944 and 1964 then 'Baby_Boomers'
                when  AnoNascimento between 1965 and 1979 then 'Geração_X'
                when  AnoNascimento between 1980 and 1994 then 'Millennials'
                when  AnoNascimento between 1995 and 2015 then 'Geração_Z'
                else 'outra_geração'
            end as Geracao,
            count(*) as quantidade
        from
            pessoas
        where
            AnoNascimento between 1944 and 2015
        group by
            Pais, Geracao
        order by
            Geracao, Pais

    """

    resultado = spark.sql(consulta)
    resultado.show()

