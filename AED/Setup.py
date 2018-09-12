import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display


# CSV's
expvida = pd.read_csv("/home/ggfl/Github/DataScienceProjects/AED/Data/life_expec/API_SP.DYN.LE00.IN_DS2_en_csv_v2_10081006.csv",index_col=0,skiprows=[0,1,2],)
expvida = expvida.drop(['Indicator Name', 'Indicator Code', 'Country Code'],axis=1).dropna(axis=1,how='all')

gdp = pd.read_csv("/home/ggfl/Github/DataScienceProjects/AED/Data/GDP/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_10080925.csv",index_col=0,skiprows=[0,1,2],)
gdp = gdp.drop(['Indicator Name', 'Indicator Code', 'Country Code', '2015'],axis=1).dropna(axis=1,how='all')

# Primeiro vamos melhorar a vizualização de dados, juntando ambas as tabelas e deixando a vizualação vertical
expv_pib = pd.merge(expvida,gdp,left_index=True, right_index=True, suffixes=['_ev','_pib'])
expv_pib = expv_pib.reset_index()
expv_pib  = pd.melt(expv_pib,id_vars='Country Name')
expv_pib.rename(columns={'Country Name':'country'}, inplace=True)
expv_pib.set_index('country',inplace=True)

# Agora para a Estatística!
    # Média
expvida.mean(axis=0)
expvida.mean(axis=1,skipna=True).sort_values(ascending=False).head(10)

    # Mediana
gdp.median(axis=0)
gdp.apply(lambda x: pd.Series({'mediana': x.median(), 'media': x.mean()})).T

    # Moda e Moda em bins
expvida.mode(axis=0)
expvida.apply(lambda x: pd.cut(x,bins=[0,50,70,np.infty],right=False)).mode().T

    # Variância de Desvio Padrão
gdp.std()
expvida.apply(lambda x: pd.Series({'media':x.mean(), 'desvp':x.std()},index=['media','desvp']),axis=1)

    # Covariância
d = pd.concat([expvida['1960'],gdp['1960']],keys=['expvida','pib'],axis=1)
d.cov()

    # Correlação
d.corr()
d.corr(method='spearman')

    # Amplitude ptp
gdp.apply(lambda x: pd.Series({'amplitude': x.ptp(), 'min':x.min(), 'max':x.max()})).T

    # Quantis
expvida.quantile([0.25, .5, .75]).T

    # Os 5 dados que "sumarizam"
expvida.describe().T
