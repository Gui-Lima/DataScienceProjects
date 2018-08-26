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
avaliacoes[10:15]

# Nao e possivel combinar selecao de linha e coluna diretamente via []
# NAO PODE - avaliacoes[1:5,'rating']

# A selecao de porcoes especificas sao feitas atraves dos atributos
# loc permite selecao por labels
avaliacoes.loc[10:15,'rating']

# iloc permite a selecao por indice
filmes.iloc[:5,[1,2,4]]


# Ainda podemos selecionar os dados com mascaras 
# booleanas como em NumPy
usuarios[(usuarios.age > 40) & 
         ~(usuarios.occupation.isin(['none','other']))].head()

#--------------------------------------------------- EXERCICIOS ------------------------------------------------------------------
#   Mostre a média de idade das mulheres cientistas
#   Quantos filmes de animação foram lançados em 1968

resposta1 = usuarios[(usuarios.occupation.isin(['scientist'])) & (usuarios.gender == 'F')]
resposta2 = filmes[(filmes.Animation == 1) & filmes.release_date.str.contains('1968')]

#--------------------------------------------------------------------------------------------------------------------------------------

# We can alter the images and add values. Be careful about that though!
c2 = resposta1.copy()
c2.iloc[0,1] = -1
c2.loc[:,'zip_code'] = None
c2.head()

# Also, there is some pretty neat things you can do to access data, or create new columns/rows
filmes['release_year'] = filmes.release_date.apply(
        lambda x: not x is np.nan and 
    re.search("\d+\-\w+\-(\d+)",str(x)).group(1) or None)


# Pandas conta com várias funções pré-definidas para obter estatísticas e informações básicas dos dados
# Ela conta também, como vimos anteriormente, com uma função apply que aplica uma função aos elementos
usuarios.age.median()
piorAvaliacao = avaliacoes.rating.values.argmin()
filmes[filmes.movie_id == avaliacoes.movie_id.iloc[piorAvaliacao]].movie_title.iloc[0]
avaliacoes.rating.value_counts()


# A forma mais simples de juntar diferentes dados e concatenacao
A = pd.Series(["A{}".format(a) for a in range(4)],
              index=range(4), name="A")
B = pd.Series(["B{}".format(a) for a in range(4)],
              index=range(4), name= "B")
C = pd.Series(["C{}".format(a) for a in range(5)],
              index=range(5), name= "C")
pd.concat([A,B,C],axis=1)

# Mas uma forma melhor e mais rápida é com merge
avaliacaoFilmes = pd.merge(avaliacoes,
                           filmes[["movie_id","movie_title",
                                   "release_year"]], 
                           on="movie_id")
avaliacaoFilmes.tail()


#---------------------------------------------------------- EXERCICIOS ----------------------------------------------------
# Calcule a média e desvio padrão das avaliações dadas aos filmes da década de 80 por programadores












