import pandas as pd
import numpy as np

# Data Sets
usuarios = pd.read_csv(
    "/home/ggfl/Github/DataScienceProjects/Atividade 0 - Training/DataSets/ml-100k/u.user",
    sep='|',header=None, names=["user_id", "age", "gender", "occupation", "zip_code"])

filmes = pd.read_csv(
    "/home/ggfl/Github/DataScienceProjects/Atividade 0 - Training/DataSets/ml-100k/u.item",
    sep='|',header=None, names=["movie_id", "movie_title",  "release_date", "video_release_date", "IMDb_URL", "unknown", "Action", "Adventure", "Animation", 
        "Children", "Comedy", "Crime", "Documentary", "Drama", "Fantasy","FilmNoir", "Horror", "Musical", "Mystery", "Romance", "SciFi","Thriller", "War", "Western"],
    encoding='latin1')

avaliacoes = pd.read_csv(
    "/home/ggfl/Github/DataScienceProjects/Atividade 0 - Training/DataSets/ml-100k/u.data",
    sep='\t',header=None, names=["user_id", "movie_id", "rating", "timestamp"])


# Oque queremos é mudar os tipos das colunas para oque eles realmente representam, em se tratando desses atributos:
#    nominal
#    binário
#    ordinal
#    numérico


def changeColumnToCategory(column):
    column = column.astype('category')
    return column

changeColumnToCategory(usuarios.gender)
changeColumnToCategory(usuarios.occupation)
changeColumnToCategory(usuarios.zip_code)


# Vemos que a de Filmes está muito errada algumas coisas

filmes.release_date = pd.to_datetime(filmes.release_date, format="%d-%b-%Y")
