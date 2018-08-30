import pandas as pd
import numpy as np
import scipy as scp
from bs4 import BeautifulSoup
import requests as rq
import re


urlS8Page = "/home/ggfl/Github/DataScienceProjects/Data Scrapping/DataSets/galaxyS8PageZoom"
urlJ7Page = "/home/ggfl/Github/DataScienceProjects/Data Scrapping/DataSets/galaxyJ7PageZoom"
urlS7Page = "/home/ggfl/Github/DataScienceProjects/Data Scrapping/DataSets/galaxyS7PageZoom"
parsed_page = BeautifulSoup(open(urlS8Page),"html.parser")

regexSamsung = "(Galaxy (?:S|J|A)\d(?:\s20\d\d)?(?:\sPlus|\sPro|\sPrime\d*|\sNeo|\sMetal|\sDuo|\sEdge(?:\sBlack Piano)?)?)\s*(?:(?:SM-)?(?:G|J|A)?(?:\d*[A-Z]*)?)?\s*(?:\dGB\s*RAM)?\s*(\d\d+)GB(?:\s\d+G)?"

allProducts = parsed_page.findAll('a', {'class':"name-link"})
allPrices = parsed_page.findAll('a', {'class':"price-label"})
allPriceContainers = parsed_page.findAll('div', {'class' : "price-container"})

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

def getAvailability():
    disponibilidade = []
    for a in allPriceContainers:
        notAvailiable = a.find('span', {'class' : "sold-out"})
        available = a.find('span', {'class' : "storeCount-txt"})
        if available:
            filteredAvailability = re.sub('[a-zA-Z\$\s\.]+','',available.text)
            disponibilidade.append(filteredAvailability)
        if notAvailiable:
            disponibilidade.append(0)
    return disponibilidade

def getLowestPrice():
    menorPreco = []
    for a in allPriceContainers:
        notAvailiable = a.find('span', {'class' : "sold-out"})
        availiable = a.find('a', {'class' : "price-label"})
        if availiable:
            filteredPrice = precoToFloat(availiable.text)
            menorPreco.append(filteredPrice)
        if notAvailiable:
            menorPreco.append(0.0)
    return menorPreco

def getList():
    numberOfFinds = len(parsed_page.findAll('a', {'class':"name-link"}))
    listCelulares = []
    modelos = getModel()
    capacidades = getCapacity()
    menorPrecos = getLowestPrice()
    disponibilidade = getAvailability()
    for i in range(numberOfFinds):
        listCelulares.append(dict(zip(['modelo','capacidade','menorPreco','disponibilidade'],[modelos[i],int(capacidades[i]),menorPrecos[i], int(disponibilidade[i])])))
    return listCelulares

def getDataFrame():
    dataCelulares = pd.DataFrame(getList(), columns=['modelo','capacidade','menorPreco','disponibilidade'])
    return dataCelulares

