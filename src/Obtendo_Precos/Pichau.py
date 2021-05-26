from bs4 import BeautifulSoup
import requests
import re
from ferramentas import cleanPrice,cleanMemory
PICHAU ={}

def getName(array_text):
    for x in range(len(array_text)):
        if (array_text[x] == "GTX") or (array_text[x] == "RTX"):
            nome = array_text[x] + " " + array_text[x+1]
            return nome
        elif (array_text[x] == "RX"):
            if array_text[x+2] == "XT":
                nome = array_text[x+1] + " " + array_text[x+2]
                return nome
            else:
                nome = array_text[x+1]
                return nome

def getMemory(array_text):
    x = 0
    for x in range(len(array_text)):
        memoria = cleanMemory(array_text[x],array_text[x-1])
        if memoria != None:
            return memoria

        
def getPage(soup):
    body = soup.body
    div1 = body.contents[2]
    main = div1.contents[1]
    div2 = main.contents[1]
    div3 = div2.contents[0]
    div4 = div3.contents[0]
    return div4

def getPrice(soup,index):
    div4 = getPage(soup)
    div5 = div4.contents[2] 
    div6 = div5.contents[index]
    a1 = div6.contents[0]
    div7 = a1.contents[0]
    div8 = div7.contents[1]
    div9 = div8.contents[1]
    if div9.get_text() != "Esgotado":
        div10 = div9.contents[0]
        div11 = div10.contents[0]
        div12 = div11.contents[1]
        preco = div12.get_text()
        valor = cleanPrice(preco,",")
        return valor
    else:
        return "Produto indisponivel"


def makeDictionary(page):
    URL = "https://www.pichau.com.br/hardware/placa-de-video?p="+page+"&product_list_limit=48&product_list_order=price_desc"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content,'html.parser')  
    z = len(PICHAU)
    x = len(PICHAU)
    html = soup.h2
    w = 0
    while (z < (48 + z)) and (html != None):
        heading = html.text
        heading_array = heading.split()
        nome = getName(heading_array)
        memoria = getMemory(heading_array)
        preco = getPrice(soup,w)
        if nome != None: 
            PICHAU[x] = x
            y = {}
            y['nome'] = nome
            y['memoria'] = memoria
            y['preco'] = preco
            PICHAU[x] = y
            x = x + 1
        z = z+ 1
        w = w + 1
        html = html.find_next("h2")
            
def getLastPage():
    URL = "https://www.pichau.com.br/hardware/placa-de-video?p=1&product_list_limit=48&product_list_order=price_desc&sort=price-desc"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content,'html.parser') 
    div4 = getPage(soup)
    nav1 = div4.contents[3]
    ul1 = nav1.contents[0]
    li1 = ul1.contents[7]
    button1 = li1.contents[0]
    page = button1.get_text()
    page = int(page)
    return page

def attDictionary():
    page = getLastPage()
    indisponivel = False

    print("atualizando dicionario...")
    for x in range(1,page):
        if indisponivel == False:
            string = str(x)
            makeDictionary(string)
            print("\nlen(PICHAU): ",len(PICHAU))
        if PICHAU[len(PICHAU)-1]['preco'] == "Produto indisponivel":
            indisponivel = True
attDictionary()

for item in PICHAU:
    print(PICHAU[item])