from bs4 import BeautifulSoup
import requests
import re
from ferramentas import number_array_to_value,check_array
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

# def getPrice(array_text):
#     first = True
#     x = 0
#     text = ""
#     while x < len(array_text) and first == True:
#         if array_text[x] == "vista":
#             first = False
#             text = array_text[x+1]
#         x = x + 1
#     if first == False:
#         array = [None]*len(text)
#         for x in range(len(text)):
#             array[x] = text[x]
#         if check_array(array,".") == True:
#             array.remove(".")
#         array.remove("R")
#         array.remove("$")
#         for x in range(len(array)):
#             if array[x] == ",":
#                 posicao = x
#             else:
#                 array[x] = float(array[x])
#         preco = number_array_to_value(array,posicao)
#         return preco
#     else:
#         return "Produto indisponivel"

def getPrice(preco):
    array = []
    for x in range(len(preco)):
        array.append(preco[x])
    array.remove("R")
    array.remove("$")
    if check_array(array,".") == True:
            array.remove(".")
    for x in range(len(array)):
        if array[x] == ',':
            posicao = x
        else:
            array[x] = float(array[x])
    value = number_array_to_value(array,posicao)
    return value


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

def find_next(caracteristica,attrs):
    secao = caracteristica.find_next(attrs)
    return secao

def makeDictionary(page):
    URL = "https://www.pichau.com.br/hardware/placa-de-video?p="+page+"&product_list_limit=48&product_list_order=price_desc"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content,'html.parser')  
    z = len(PICHAU)
    position = []*z
    x = len(PICHAU)
    html = soup.h2
    initlen = len(PICHAU)
    while (z < (48 + initlen)) and (html != None):
        heading = html.text
        heading_array = heading.split()
        nome = getName(heading_array)
        memoria = getMemory(heading_array)
        position.append(0)
        if nome != None:
            position[z] = 1 
            PICHAU[x] = x
            y = {}
            y['nome'] = nome
            y['memoria'] = memoria
            y['preco'] = "Produto indisponivel"
            PICHAU[x] = y
            x = x + 1
        z = z+ 1
        html = find_next(html,"h2")
    x = 0
    body = soup.body
    div1 = body.contents[2]
    main = div1.contents[1]
    div2 = main.contents[1]
    div3 = div2.contents[0]
    div4 = div3.contents[0]
    div5 = div4.contents[2]
    y = initlen
    for x in range(z+y):
        print("\nx: ",x)
        print("\nlen(position)",len(position))
        if position[x] == 1:
            div6 = div5.contents[x]
            a1 = div6.contents[0]
            div7 = a1.contents[0]
            div8 = div7.contents[1]
            div9 = div8.contents[1]
            if div9.get_text() != "Esgotado":
                div10 = div9.contents[0]
                div11 = div10.contents[0]
                div12 = div11.contents[1]
                preco = div12.get_text()
                valor = getPrice(preco)
                PICHAU[y]['preco'] = valor
            else:
                PICHAU[y]['preco'] = "Produto indisponivel"
            y = y + 1
            
def getLastPage():
    URL = "https://www.pichau.com.br/hardware/placa-de-video?p=1&product_list_limit=48&product_list_order=price_desc&sort=price-desc"
    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content,'html.parser') 
    body = soup.body
    div1 = body.contents[2]
    main = div1.contents[1]
    div2 = main.contents[1]
    div3 = div2.contents[0]
    div4 = div3.contents[0]
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