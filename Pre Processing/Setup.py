import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from sklearn.preprocessing import StandardScaler, MinMaxScaler

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


# A de usuários podemos mudar as colunas categoricas
def changeColumnToCategory(column):
    column = column.astype('category')
    return column

usuarios.gender = changeColumnToCategory(usuarios.gender)
usuarios.occupation = changeColumnToCategory(usuarios.occupation)
usuarios.zip_code = changeColumnToCategory(usuarios.zip_code)


# Vemos que a de Filmes está muito errada algumas coisas
#print(filmes.dtypes)

filmes.release_date = pd.to_datetime(filmes.release_date, format="%d-%b-%Y")

filmes.iloc[:,5:] = filmes.iloc[:,5:].astype('bool')
filmes.iloc[:,5:].apply(pd.value_counts)


# Nas avaliações, vamos usar categorias do import
avaliacoes.rating = avaliacoes.rating.astype(CategoricalDtype(categories=avaliacoes.rating.unique().sort(),ordered=True))

avaliacoes.timestamp = pd.to_datetime(avaliacoes.timestamp,unit='s')

# Agora vamos tratar de alguns outros detalhes, como Nan's e coisas que podem atrapalhar o processamento de dados
    # Podemos tirar os nans
filmes.dropna(subset=['release_date','IMDb_URL'])
filmes.dropna(axis=1,how='all')
    # Podemos substituir os nans
filmes.release_date.fillna(value=filmes.release_date.mode()[0])[266]

# Outra etapa de pre processamento é deixar os dados da maneria que você quer

    # Dividindo em bins
filmes['decada'] = pd.cut(filmes.release_date.map(lambda x: x.year),
       bins=np.insert(np.linspace(1940,2000,7,dtype=np.int32),0,1920),
        labels=["20s"]+list(map(lambda x: '{}s'.format(x%100),
       np.linspace(1940,2000,7,dtype=np.int32)[:6])))

    # Normalizando
wine = pd.read_csv("http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv",sep=';')

scaler = MinMaxScaler()
pd.DataFrame(scaler.fit_transform(wine.drop('quality',axis=1)), columns=wine.drop('quality',axis=1).columns)

wine.drop('quality',axis=1).apply(lambda x: (x-x.mean())/x.std()).describe()

wineCopy = wine.copy().drop('quality',axis=1)
scaler = StandardScaler().fit(wineCopy)
wineCopy.iloc[:,:] = scaler.fit_transform(wineCopy)
