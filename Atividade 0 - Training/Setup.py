# Good imports
import numpy as np
import scipy as sp
import pandas as pd
import re
from IPython.display import display


# Importing the DataSets
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



# ------------------------------------------ USEFUL COMMANDS ----------------------------------

# Selecionando uma coluna
usuarios['age'].head()
usuarios.age.head()

# Selecionando multiplas colunas
usuarios[['age','gender']].head()

# Selecionando linhas com slice - Os Slices criam uma visão, então é uma referência, se alterada, altera o original
display(avaliacoes[10:15])

# Nao e possivel combinar selecao de linha e coluna diretamente via []
# NAO PODE - avaliacoes[1:5,'rating']

# A selecao de porcoes especificas sao feitas atraves dos atributos
# loc permite selecao por labels
avaliacoes.loc[10:15,'rating']

# iloc permite a selecao por indice
display(filmes.iloc[:5,[1,2,4]])





