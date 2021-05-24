from bs4 import BeautifulSoup
import requests
import re

dicionario ={}
def arredondar(num):
    return float( '%g' % (num))

def number_array_to_value(array,posicao):
    letra = 0
    first = False
    for x in range(posicao):
        array[x] = array[x]*pow(10,posicao - 1 - x)
    for x in range(posicao + 1,len(array)):
        if (type(array[x]) == float) or (type(array[x]) == int):
            array[x] = array[x]*pow(10,posicao - x)
        elif (type(array[x]) != float) and (type(array[x]) != int) and first == False:
            letra = x
            first = True
            x = len(array)
    if letra == 0:
        valor = 0.0
        for z in range(len(array)):
            if z != posicao:
                valor = arredondar(valor + array[z])
    else:
        valor = 0.0
        for z in range(letra):
            if z != posicao:
                valor = arredondar(valor + array[z])  
    return valor

def getName(array_text):
    for x in range(len(array_text)):
        if (array_text[x] == "GTX") or (array_text[x] == "RTX") or (array_text[x] == "RX"):
            nome = array_text[x] + " " + array_text[x+1]
            return nome
def check_array(array,item):
    teste = False
    for x in range(len(array)):
        if array[x] == item:
            teste = True
    return teste

def getPrice(array_text):
    first = True
    x = 0
    text = ""
    while x < len(array_text) and first == True:
        if array_text[x] == "vista":
            first = False
            text = array_text[x+1]
        x = x + 1
    if first == False:
        array = [None]*len(text)
        for x in range(len(text)):
            array[x] = text[x]
        if check_array(array,".") == True:
            array.remove(".")
        array.remove("R")
        array.remove("$")
        for x in range(len(array)):
            if array[x] == ",":
                posicao = x
            else:
                array[x] = float(array[x])
        preco = number_array_to_value(array,posicao)
        return preco
    else:
        return "Produto indisponivel"
def getMemory(array_text):
    first = True
    x = 0
    while (x < len(array_text)) and (first == True):
        if (array_text[x] == "GTX") or (array_text[x] == "RTX") or (array_text[x] == "RX"):   
            first == False 
            for y in range(x,len(array_text)):
                array = array_text[y]
                primeiro = True
                z = 0
                while (z < len(array) - 1) and primeiro == True :
                    if array[z] == "G" and array[z+1] == "B":
                        primeiro = False
                        try:
                            memoria = int(array[0])*10 + int(array[1])
                            return memoria
                        except:
                            memoria = int(array[0])
                            return memoria

                    z = z + 1 
        x = x + 1

def makeDictionary(page):
    URL = "https://www.pichau.com.br/hardware/placa-de-video?p="+page+"&product_list_limit=48&product_list_order=price_desc"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content,'html.parser')  
    x = len(dicionario)
    for tag in soup.find_all('div',class_="product details product-item-details"):
        heading = tag.text
        heading_array = heading.split()
        if (getName(heading_array) != None) or (getPrice(heading_array) != "Produto indisponivel"): 
            dicionario[x] = x
            y = {}
            y['nome'] = getName(heading_array)
            y['memoria'] = getMemory(heading_array)
            y['preco'] = getPrice(heading_array)
            dicionario[x] = y
            x = x + 1
            
                
def getLastPage():
    URL = "https://www.pichau.com.br/hardware/placa-de-video?p=1&product_list_limit=48&product_list_order=price_desc"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content,'html.parser') 
    page = soup.find('span',class_="text-page last").get_text()
    page = int(page)
    return page
def attDictionary():
    page = getLastPage()
    indisponivel = False
    for x in range(1,page+1):
        if indisponivel == False:
            string = str(x)
            makeDictionary(string)
        if dicionario[len(dicionario)-1]['preco'] == "Produto indisponivel":
            indisponivel = True
attDictionary()
for item in dicionario:
    print(dicionario[item])