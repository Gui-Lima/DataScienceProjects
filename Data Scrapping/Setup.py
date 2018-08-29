import pandas as pd
import numpy as np
import scipy as scp
from bs4 import BeautifulSoup
import requests as rq
import re

url = "/home/ggfl/Github/DataScienceProjects/Data Scrapping/DataSets/galaxyS8PageZoom"
parsed_page = BeautifulSoup(open(url),"html.parser")


regexSamsung = "(Galaxy S\d(?:\sPlus)?)\s*SM-G(?:\d+[a-zA-Z]*)\s*(?:\dGB\s*RAM)*\s*(\d+)GB"


def getModel():
    modelo = []
    for a in parsed_page.findAll('a', {'class':"name-link"}):
        filteredName = re.sub('Smartphone Samsung ', '', a.text)
        modelo.append(re.match(regexSamsung, filteredName).group(1))
    return modelo

def getCapacity():
    capacidade = []
    for a in parsed_page.findAll('a', {'class':"name-link"}):
        filteredName = re.sub('Smartphone Samsung ', '', a.text)
        capacidade.append(re.match(regexSamsung, filteredName).group(2))
    return capacidade

def getList():
    numberOfFinds = len(parsed_page.findAll('a', {'class':"name-link"}))
    listCelulares = []
    modelos = getModel()
    capacidades = getCapacity()
    for i in range(numberOfFinds):
        listCelulares.append(dict(zip(['modelo','capacidade'],[modelos[i],int(capacidades[i])])))
    return listCelulares
