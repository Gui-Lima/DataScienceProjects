import pandas as pd
import numpy as np
import scipy as scp
from bs4 import BeautifulSoup
import requests as rq
import re

url = "/home/ggfl/Github/DataScienceProjects/Data Scrapping/DataSets/galaxyS8PageZoom"
parsed_page = BeautifulSoup(open(url),"html.parser")

for a in parsed_page.findAll('a', {'class':"name-link"}):
    regexSamsung = "(Galaxy S\d(?:\sPlus)?)\s*SM-G(?:\d+[a-zA-Z]*)\s*(?:\dGB\s*RAM)*\s*(\d+)GB"
    teste = re.sub('Smartphone Samsung ', '', a.text)
    modelo, capacidade = re.match(regexSamsung, teste).groups()
