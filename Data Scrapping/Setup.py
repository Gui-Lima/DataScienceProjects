import pandas as pd
import numpy as np
import scipy as scp
from bs4 import BeautifulSoup
import requests as rq
import re

url = "/home/ggfl/Github/DataScienceProjects/Data Scrapping/DataSets/galaxyS8PageZoom"
parsed_page = BeautifulSoup(open(url),"html.parser")


regexSamsung = "(Galaxy S\d(?:\sPlus)?)\s*SM-G(?:\d+[a-zA-Z]*)\s*(?:\dGB\s*RAM)*\s*(\d+)GB"
allProducts = parsed_page.findAll('a', {'class':"name-link"})
allPrices = parsed_page.findAll('a', {'class':"price-label"})
allStoresAvaliable = parsed_page.findAll('span', {'class' : "storeCount-txt"})

def precoToFloat(x):
    return float(re.sub(',','.',re.sub('[a-zA-Z\$\s\.]+','',x)))

def getModel():
    modelo = []
    for a in allProducts:
        filteredName = re.sub('Smartphone Samsung ', '', a.text)
        modelo.append(re.match(regexSamsung, filteredName).group(1))
    return modelo

def getCapacity():
    capacidade = []
    for a in allProducts:
        filteredName = re.sub('Smartphone Samsung ', '', a.text)
        capacidade.append(re.match(regexSamsung, filteredName).group(2))
    return capacidade

def getLowestPrice():
    menorPreco = []
    for a in allPrices:
        filteredPrice = precoToFloat(a.text)
        menorPreco.append(filteredPrice)
    return menorPreco

def getAvailability():
    disponibilidade = []
    for a in allStoresAvaliable:
        filteredAvailability = re.sub('[a-zA-Z\$\s\.]+','',a.text)
        disponibilidade.append(filteredAvailability)
    return disponibilidade

def getList():
    numberOfFinds = len(parsed_page.findAll('a', {'class':"name-link"}))
    listCelulares = []
    modelos = getModel()
    capacidades = getCapacity()
    menorPrecos = getLowestPrice()
    disponibilidade = getAvailability()
    for i in range(numberOfFinds):
        listCelulares.append(dict(zip(['modelo','capacidade','menor preco','disponibilidade'],[modelos[i],int(capacidades[i]),menorPrecos[i], int(disponibilidade[i])])))
    return listCelulares

print(getList())