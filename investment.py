import matplotlib.pyplot as plt
import numpy as np
import json
import requests

httpGET = requests.get("https://buff.163.com/api/market/goods?game=csgo")
csrfToken = httpGET.cookies.get('csrf_token')
#test

cookies = {
    "csrf-token": csrfToken,
    "client_id":"7-h_oTfFgQT6Jj-8F1mLRA",
    "game":"csgo",
    "display_appids":"[730\054 570\054 1]",
    "Locale-Supported":"en",
    "Device-Id":"pz5W6Q9OQxiycPdvob1L",
}

def inputInvestment():
    item = input("Ny investment: ")
    antall = int(input("Hvor mange kjøpt: "))
    pris = float(input("Totalpris i rmb: "))
    buffPris = 0

    if item == 0:
        data = {
            "item": 0,
            "antall": 0,
            "pris": 0,
            "buffPris": 0,
        }
        return data

    else:
        data = {
            "item": item,
            "antall": antall,
            "pris": pris,
            "buffPris": buffPris
        }
        return data

def lastInnLagretData():
    with open("investment.json", "r") as file:
        try:
            lagretData = []
            lagretData = json.load(file)
        except FileNotFoundError:
            lagretData = []
        return lagretData

def mergeEksisterendeData(markedList, dataList):
    data = {}
    for val in dataList: #For hvert dictionaryelement i JSON-Dictionary
        key = val["item"] #Allokerer variabelen key verdien/navnet til item
        if key in data: #Hvis key eller navnet er i data
            #Oppdaterer antall og pris for allerede eksisterende investering
            data[key]['antall'] += val['antall']
            data[key]['pris'] += val['pris']
        else:
            #Legger til ny investering i json listen hvis key ikke er i data 
            data[key] = val
    
    navn = []
    priser = []

    items = markedList['data']['items']

    for val in items:
        navn.append(val['market_hash_name'])
        priser.append(val['sell_reference_price'])

    for i in range(len(navn)):
        if navn[i] in data:
            data[navn[i]]['buffPris'] = priser[i]
        else:
            pass

    return list(data.values()) 

def lagreNyData(data):
    with open("investment.json", "w") as file:
        json.dump(data, file)

def requestMarketPrice():
    response = requests.get("https://buff.163.com/api/market/goods?game=csgo", cookies=cookies) #Henter data fra markedsiden
    marketData = response.json() #Konverter responsen til json

    with open("buffprice.json", "w") as file:
        json.dump(marketData,file)

def lastInnMarkedData():
    with open("buffprice.json", "r") as file:
        try:
            lagretData = []
            lagretData = json.load(file)
        except FileNotFoundError:
            lagretData = []
        return lagretData


# Lagre eksisterende data fra JSON fila
print("Laster inn lagret data")
lagretData = lastInnLagretData()
print("Lagret data:", lagretData)

# Få tak i ny data

print("Forespør ny data")
nyData = inputInvestment()
print("Ny data", nyData)

# Legge til ny data med lagret data
print("Legger til ny data hos gammel data")
lagretData.append(nyData)
print("Ny lagret data: ", lagretData)


#Hente buff priser
print("Henter BUFF priser")
requestMarketPrice()
print("BUFF priser hentet")

#Lagre buffpriser i liste
buffPrisData = lastInnMarkedData()
#Merge alleredeeksisterende investering

print("Sjekker for duplisert investering")
prosessertData = mergeEksisterendeData(buffPrisData, lagretData)
print("Fusjonerer eventuell alleredeeksisterende investering")


# Overskrive JSON fila med ny og gammel data
print("Lagrer ny og gammel data til JSON-fila")
lagreNyData(prosessertData)
print("Data lagret", prosessertData)

#Jsonprosjekt1!
